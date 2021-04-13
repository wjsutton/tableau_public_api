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
#loc.workbooks

attributions = workbooks[workbooks['attributions'].str.len() > 0] #.reset_index()
#workbook_attributions = pd.DataFrame()
#if len(attributions)>0:
print(attributions)
#workbook_attributions = pd.json_normalize(attributions['attributions'], max_level=0)
#print(workbook_attributions)
#workbook_attributions = pd.json_normalize(workbooks['attributions'], max_level=0)
#del profile['address']
del profile['websites']
del profile['workbooks']

#print(profile)
#print(websites)
#print(workbooks)

#print(workbook_attributions)