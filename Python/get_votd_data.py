import pandas as pd
import requests
import csv
import json
import time
import os
import re
from datetime import datetime

def check_and_trigger(api_url="https://public.tableau.com/public/apis/bff/discover/v1/vizzes/viz-of-the-day?page=0&limit=12",
                      csv_file="votd_index.csv"):
    """
    Checks the API for new data based on 'workbookRepoUrl'.
    If new data is found, adds it to the CSV file.
    Returns:
        1 if new data found and added to CSV,
        0 if no new data,
       -1 if error occurs.
    """
    try:
        print(f"Checking API for new Viz of the Day data...")
        response = requests.get(api_url)
        response.raise_for_status()
        vizzes = response.json()  # This is a list

        if not isinstance(vizzes, list):
            print("Unexpected API response format")
            return -1

        # Load existing workbookRepoUrls from CSV
        existing_urls = set()
        if os.path.exists(csv_file):
            try:
                df = pd.read_csv(csv_file)
                existing_urls = set(df['workbookRepoUrl'].tolist())
                print(f"Found {len(existing_urls)} existing URLs in {csv_file}")
            except Exception as e:
                print(f"Error reading existing CSV: {e}")
                # If CSV is corrupted or empty, start fresh
                existing_urls = set()

        # Get current URLs from API
        current_urls = [viz["workbookRepoUrl"] for viz in vizzes]

        # Find new vizzes by workbookRepoUrl
        new_vizzes = [viz for viz in vizzes if viz["workbookRepoUrl"] not in existing_urls]

        if new_vizzes:
            print(f"Found {len(new_vizzes)} new visualizations")
            
            # Prepare new rows for CSV
            new_rows = []
            today_date = datetime.now().strftime('%Y-%m-%d')
            
            for viz in new_vizzes:
                # Clean HTML tags from description
                description = viz.get('description', '')
                clean_description = re.sub('<.*?>', '', description).strip()
                
                new_row = {
                    'workbookRepoUrl': viz['workbookRepoUrl'],
                    'votd_description': clean_description,
                    'votd_date': today_date
                }
                new_rows.append(new_row)
                print(f"  - Adding: {viz['workbookRepoUrl']}")

            # Append to CSV or create new file
            if os.path.exists(csv_file):
                # Append to existing CSV
                df_new = pd.DataFrame(new_rows)
                df_new.to_csv(csv_file, mode='a', header=False, index=False)
            else:
                # Create new CSV with headers
                df_new = pd.DataFrame(new_rows)
                df_new.to_csv(csv_file, index=False)
            
            print(f"Successfully added {len(new_rows)} new entries to {csv_file}")
            return 1  # New data found and added
        else:
            print("No new visualizations found")
            return 0  # No new data

    except Exception as e:
        print(f"Error checking Viz of the Day: {e}")
        return -1  # Indicate error


def run_votd_pipeline():
    """
    Main function to run the VOTD data pipeline.
    Can be called multiple times throughout the day.
    """
    print("=" * 60)
    print(f"Starting VOTD Pipeline - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    result = check_and_trigger()
    
    if result == 1:
        print("✅ Pipeline completed successfully - New data added!")
    elif result == 0:
        print("ℹ️  Pipeline completed - No new data available")
    else:
        print("❌ Pipeline failed - Check error messages above")
    
    print("=" * 60)
    return result


def check_csv_integrity(csv_file="votd_index.csv"):
    """
    Check the integrity of the CSV file and report any issues.
    """
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} does not exist yet")
        return
    
    try:
        df = pd.read_csv(csv_file)
        print(f"CSV Status:")
        print(f"  - Total rows: {len(df)}")
        print(f"  - Unique URLs: {df['workbookRepoUrl'].nunique()}")
        
        # Check for duplicates
        duplicates = df[df.duplicated(subset=['workbookRepoUrl'], keep=False)]
        if not duplicates.empty:
            print(f"  - ⚠️  WARNING: Found {len(duplicates)} duplicate URLs")
            print(duplicates[['workbookRepoUrl', 'votd_date']])
        else:
            print("  - ✅ No duplicate URLs found")
        
        # Show date range
        if 'votd_date' in df.columns:
            min_date = df['votd_date'].min()
            max_date = df['votd_date'].max()
            print(f"  - Date range: {min_date} to {max_date}")
        
    except Exception as e:
        print(f"Error checking CSV integrity: {e}")


def process_csv_with_api(input_file, output_file, delay=0.5):
    """
    Read CSV, call API for each workbookRepoUrl, flatten response, and save to new CSV.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        delay (float): Delay between API calls in seconds (be nice to the API)
    """
    # Read the input CSV
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)
    
    # Initialize list to store results
    results = []
    
    # Process each row
    for index, row in df.iterrows():
        workbook_url = row['workbookRepoUrl']
        print(f"Processing {index + 1}/{len(df)}: {workbook_url}")
        
        # Build API URL
        api_url = f"https://public.tableau.com/profile/api/single_workbook/{workbook_url}?"
        
        try:
            # Make API call
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            
            # Parse JSON response
            api_data = response.json()
            
            # Create result row with original data + flattened API response
            result_row = row.to_dict()  # Start with original CSV data
            
            # Flatten and add API response data
            for key, value in api_data.items():
                if key == 'attributions':
                    # Handle attributions specially
                    result_row = process_attributions(result_row, value)
                elif isinstance(value, (dict, list)):
                    # Handle other nested objects/arrays by converting to string
                    result_row[f"api_{key}"] = json.dumps(value)
                else:
                    result_row[f"api_{key}"] = value
            
            results.append(result_row)
            print(f"  ✓ Success")
            
        except requests.exceptions.RequestException as e:
            print(f"  ✗ API call failed: {e}")
            # Add original row even if API fails
            result_row = row.to_dict()
            # Add empty API fields to maintain consistent columns
            api_fields = ['showInProfile', 'allowDataAccess', 'showByline', 'showShareOptions', 
                         'showTabs', 'showToolbar', 'showWatermark', 'warnDataAccess', 'id', 
                         'ownerId', 'firstPublishDate', 'lastPublishDate', 'createdAt', 
                         'lastUpdateDate', 'size', 'description', 'luid', 'permalink', 
                         'revision', 'title', 'extractInfo', 'viewCount', 'defaultViewName', 
                         'defaultViewRepoUrl', 'defaultViewLuid', 'authorProfileName', 
                         'authorDisplayName', 'externalLink', 'numberOfFavorites', 'attributions']
            
            for field in api_fields:
                if field == 'attributions':
                    # Add empty attribution fields
                    result_row = process_attributions(result_row, [])
                else:
                    result_row[f"{field}"] = None
            
            results.append(result_row)
            
        except json.JSONDecodeError as e:
            print(f"  ✗ JSON parsing failed: {e}")
            # Add original row with empty API fields
            result_row = row.to_dict()
            # Add empty attribution fields for consistency
            result_row = process_attributions(result_row, [])
            results.append(result_row)
        
        # Be nice to the API
        time.sleep(delay)
    
    # Convert results to DataFrame and save
    print(f"\nSaving results to {output_file}...")
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    
    print(f"Done! Processed {len(results)} records.")
    print(f"Output saved to: {output_file}")


def process_attributions(result_row, attributions):
    """
    Process the attributions field and add individual attribution columns.
    
    Args:
        result_row (dict): The current result row dictionary
        attributions (list): List of attribution dictionaries from API response
    
    Returns:
        dict: Updated result_row with attribution fields
    """
    # Store the original attributions as JSON string
    result_row['attributions'] = json.dumps(attributions)
    
    # Add attribution T|F column
    result_row['attribution_exists'] = len(attributions) > 0 if attributions else False
    
    # Initialize all possible attribution fields to None
    attribution_fields = [
        'authorDisplayName', 'authorProfileName', 'attributionUrl', 
        'workbookName', 'workbookRepoUrl', 'workbookViewName'
    ]
    
    for field in attribution_fields:
        result_row[f'attributed_{field}'] = None
    
    # If there are attributions, process them
    if attributions and len(attributions) > 0:
        # For now, take the first attribution if multiple exist
        # You can modify this logic if you want to handle multiple attributions differently
        first_attribution = attributions[0]
        
        for field in attribution_fields:
            if field in first_attribution:
                result_row[f'attributed_{field}'] = first_attribution[field]
    
    return result_row


if __name__ == "__main__":
    # Run the pipeline
    result = run_votd_pipeline()
    
    # Check CSV integrity after running
    check_csv_integrity()
    
    # Optionally run the API processing if you want to enrich the data
    # Uncomment the line below if you want to process the CSV with additional API data
    # process_csv_with_api('votd_index.csv', 'votd_index_with_api_data.csv')