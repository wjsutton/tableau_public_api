import json
import pandas as pd
import urllib3

# do API call to search for top 20 "maps" from Tableau Public search
api_call = "https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes"
http = urllib3.PoolManager()
search_call = json.loads(http.request('GET',api_call).data)

# convert json to dataframe structure just for search reults
df = pd.json_normalize(search_call['results'], max_level=0)

# Not there are additional nodes in the data frame so  we need to
# normalise more nodes to get details of workbooks and authors
workbook_meta = pd.json_normalize(df['workbookMeta'], max_level=0)
workbooks = pd.json_normalize(df['workbook'], max_level=0)

# concat normalized nodes together
search_results = pd.concat([workbook_meta,workbooks], axis=1)

# delete unneccessary column
del search_results['viewInfos']

print(search_results)

# Save locally
search_results.to_csv('tableau_public_search_results.csv', index=False)

