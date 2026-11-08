import json
import pandas as pd
import urllib3

# do API call to search for top 20 "maps" from Tableau Public search
api_call = "https://public.tableau.com/public/apis/bff/v2/search/query-workbooks?count=20&query=maps&start=0"
http = urllib3.PoolManager()
search_call = json.loads(http.request('GET',api_call).data)

# convert json to dataframe structure just for search reults
df = pd.json_normalize(search_call['results'], max_level=0)

# Not there are additional nodes in the data frame so  we need to
# normalise more nodes to get details of workbooks and authors
search_results = pd.json_normalize(df['workbook'], max_level=0)

print(search_results)

# Save locally
search_results.to_csv('tableau_public_search_results.csv', index=False)

