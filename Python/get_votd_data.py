import json
import pandas as pd
import urllib3
import numpy as np
import re

# Do an API call to find the total number of VOTDs for loop
http = urllib3.PoolManager()
# initialise dataframe
votd_df =[]

# Loop and extract VOTD data (API only allows limit=1 or 12; next == -1 at the end)
start = 0
while start != -1:
    print(start)
    votd = json.loads(http.request('GET',"https://public.tableau.com/public/apis/bff/discover/v2/vizzes/viz-of-the-day?startIndex=" + str(start) + "&limit=12").data)
    df = pd.json_normalize(votd['contents'], max_level=1)
    votd_df.append(df)
    start = votd['next']

# Combine data frames from loop
votd_df = pd.concat(votd_df)

# Save locally
votd_df.to_csv('tableau_public_votd.csv', index=False)
print(votd_df)
