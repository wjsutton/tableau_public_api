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
workbooks_call = 'https://public.tableau.com/public/apis/workbooks?profileName=' + your_username + '&start=0&count=50&visibility=NON_HIDDEN'
workbooks = pd.json_normalize(json.loads(http.request('GET',workbooks_call).data)['contents'], max_level=0)



del profile['websites']

print(workbooks)

print(profile)
print(tableau_profile['address'])
#address = pd.json_normalize(tableau_profile['address'])
#print(address)
#print(tableau_profile['address']['state'])
#print(tableau_profile['address']['city'])
