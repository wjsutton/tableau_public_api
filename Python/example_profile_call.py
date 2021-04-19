# TO DO 
# Parse out profile address data fields
# can take options: country, state, city but each can also be empty but not quoted


import json
import urllib3
import pandas as pd

http = urllib3.PoolManager()

your_username = 'wjsutton'
profile_call = "https://public.tableau.com/profile/api/" + your_username


tableau_profile = json.loads(http.request('GET',profile_call).data)
profile = pd.json_normalize(tableau_profile, max_level=0)
#address = pd.json_normalize(tableau_profile['address'], max_level=0)
websites = pd.json_normalize(tableau_profile['websites'], max_level=0)
workbooks = pd.json_normalize(tableau_profile['workbooks'], max_level=0)


# Finding attributions and merging to workbooks
attributions_df = []
for i in workbooks.index:
    attributions = pd.json_normalize(workbooks['attributions'][i])
    if len(attributions) > 0:
        attributions.columns = 'attribution_' + attributions.columns
        attributions['workbookRepoUrl'] = workbooks['workbookRepoUrl'][i]
        attributions_df.append(attributions)

if len(attributions_df) > 0:
    attributions_df = pd.concat(attributions_df)
    workbooks = pd.merge(workbooks,attributions_df, on='workbookRepoUrl', how='left')

del profile['websites']
del profile['workbooks']

print(workbooks)

print(profile)
print(tableau_profile['address'])
#address = pd.json_normalize(tableau_profile['address'])
#print(address)
#print(tableau_profile['address']['state'])
#print(tableau_profile['address']['city'])
