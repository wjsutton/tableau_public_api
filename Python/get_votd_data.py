import json
import pandas as pd
import urllib3
import numpy as np
import re

http = urllib3.PoolManager()
votd = json.loads(http.request('GET',"https://public.tableau.com/api/gallery?page=0&count=10000&galleryType=viz-of-the-day&language=any").data)
df = pd.json_normalize(votd['items'], max_level=0)

# initialise dataframes
workbook_df =[]
attributions_df = []

for i in df.index:
    print(i)
    workbook_url = 'https://public.tableau.com/profile/api/single_workbook/' + votd['items'][i]['workbookRepoUrl']
    workbook = json.loads(http.request('GET',workbook_url).data)
    workbook = pd.json_normalize(workbook)
    
    if 'error.message' in workbook.columns:
        source_url = df['sourceUrl'][i]
        retry = re.search('/views/(.+?)/', source_url)
        if retry is not None:
            retry = retry.group(0)[7:-1]
            workbook_url = 'https://public.tableau.com/profile/api/single_workbook/' + retry
            workbook = json.loads(http.request('GET',workbook_url).data)
            workbook = pd.json_normalize(workbook)
            workbook['workbookRepoUrl'] = votd['items'][i]['workbookRepoUrl']

    if 'error.message' not in workbook.columns:
        attributions = pd.json_normalize(workbook['attributions'][0])
        attributions['workbookRepoUrl'] = votd['items'][i]['workbookRepoUrl']

        workbook_df.append(workbook)
        attributions_df.append(attributions)

# see pd.concat documentation for more info
workbook_df = pd.concat(workbook_df)
attributions_df = pd.concat(attributions_df)

# join VOTD with workbook and attributions dataframes
df = pd.merge(df,workbook_df, on='workbookRepoUrl',how='left')
df = pd.merge(df,attributions_df, on='workbookRepoUrl',how='left')

# remove columns that have been json_normalized to additional columns
del df['workbook']
del df['attributions']

# if there are error messages remove them
if 'error.message' in df.columns:
    del df['error.message']
    del df['error.id']

# convert lists to comma seperated strings
df['types'] = [','.join(map(str, l)) for l in df['types']]
df['topics'] = [','.join(map(str, l)) for l in df['topics']]
df['badges'] = [','.join(map(str, l)) for l in df['badges']]

# rename attribution columns
df.rename(columns={'authorProfileName_y':'attributed_authorProfileName'}, inplace=True)
df.rename(columns={'workbookName':'attributed_workbookName'}, inplace=True)
df.rename(columns={'authorDisplayName':'attributed_authorDisplayName'}, inplace=True)
df.rename(columns={'workbookViewName':'attributed_workbookViewName'}, inplace=True)

# rename conflicts between gallery and workbook data
df.rename(columns={'authorProfileName_x':'authorProfileName'}, inplace=True)
df.rename(columns={'title_x':'gallery_title'}, inplace=True)
df.rename(columns={'description_x':'gallery_description'}, inplace=True)
df.rename(columns={'title_y':'viz_title'}, inplace=True)
df.rename(columns={'description_y':'viz_description'}, inplace=True)

df = df.drop_duplicates()

# Save locally
#df.to_csv('data/tableau_public_votd.csv', index=False)
print(df)
