import json
import urllib3
import pandas as pd
import math

http = urllib3.PoolManager()

fa_call = 'https://public.tableau.com/s/authors/list/feed?'
fa_json = json.loads(http.request('GET',fa_call).data)
featured_authors = pd.json_normalize(fa_json['authors'])

n_featured_authors = len(featured_authors)
author_loops = range(n_featured_authors)

# initialise dataframes
profile_df =[]
websites_df =[]
workbook_df =[]

for i in range(n_featured_authors):
    your_username = featured_authors['profile_name'][i]
    print("Working on " + featured_authors['profile_name'][i] +"'s profile")
    profile_call = "https://public.tableau.com/profile/api/" + your_username

    tableau_profile = json.loads(http.request('GET',profile_call).data)
    profile = pd.json_normalize(tableau_profile, max_level=0)
    profile['author_description'] = featured_authors['author_description'][i]

    del profile['websites']
    if 'address' in profile.columns:
        del profile['address']

    profile_df.append(profile)

    websites = pd.json_normalize(tableau_profile['websites'], max_level=0)
    websites['profileName'] = your_username
    websites_df.append(websites)

    n_workbooks = profile['visibleWorkbookCount']
    workbook_loops = math.ceil(n_workbooks / 50) 

    for j in range(workbook_loops):
        print('Getting workbooks page: ' + str(j))
        start = j * 50
        workbook_call = 'https://public.tableau.com/public/apis/workbooks?profileName=' + your_username + '&start='+str(start)+'&count=50&visibility=NON_HIDDEN'
        tableau_workbooks = json.loads(http.request('GET',workbook_call).data)
        workbooks = pd.json_normalize(tableau_workbooks['contents'], max_level=0)
        workbooks['profileName'] = your_username
        workbook_df.append(workbooks)

# Combine data frames from loop
profile_df = pd.concat(profile_df)
workbook_df = pd.concat(workbook_df)
websites_df = pd.concat(websites_df)

# Get VOTD data
votd = json.loads(http.request('GET',"https://public.tableau.com/api/gallery?page=0&count=100&galleryType=viz-of-the-day&language=any").data)
votd_count = votd['totalItems']

# Number of pages for VOTD loop
end = math.ceil(votd_count/100)
pages = range(end)

# initialise dataframe
votd_df =[]

# Loop and extract VOTD data
for i in pages:
    print('Getting VOTDs page: ' + str(i))
    votd = json.loads(http.request('GET',"https://public.tableau.com/api/gallery?page=" + str(i) + "&count=100&galleryType=viz-of-the-day&language=any").data)
    df = pd.json_normalize(votd['items'], max_level=1)
    votd_df.append(df)

# Combine data frames from loop
votd_df = pd.concat(votd_df)

votd_df['VOTD_flag'] = 'VOTD'
votd_lookup = votd_df[['workbookRepoUrl','VOTD_flag']]

workbook_df = pd.merge(workbook_df,votd_lookup,how='left',on='workbookRepoUrl')

# Save locally
profile_df.to_csv('fa_profiles.csv', index=False)
workbook_df.to_csv('fa_workbooks.csv', index=False)
websites_df.to_csv('fa_websites.csv', index=False)
