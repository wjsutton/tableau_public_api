import json
import pandas as pd
import urllib3
import numpy as np
import re

# Do an API call to find the total number of VOTDs for loop
http = urllib3.PoolManager()
votd = json.loads(http.request('GET',"https://public.tableau.com/api/gallery?page=0&count=100&galleryType=viz-of-the-day&language=any").data)
votd_count = votd['totalItems']

# Number of pages for VOTD loop
end = int(votd_count/100) + 1
pages = range(end)

# initialise dataframe
votd_df =[]

# Loop and extract VOTD data
for i in pages:
    print(i)
    votd = json.loads(http.request('GET',"https://public.tableau.com/api/gallery?page=" + str(i) + "&count=100&galleryType=viz-of-the-day&language=any").data)
    df = pd.json_normalize(votd['items'], max_level=1)
    votd_df.append(df)

# Combine data frames from loop
votd_df = pd.concat(votd_df)

# Save locally
votd_df.to_csv('tableau_public_votd.csv', index=False)
print(votd_df)
