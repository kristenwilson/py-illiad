import requests
import json
import sys
from config import api_key, api_base

user_id = '' # Enter the external user ID here
api_url = api_base + '/Users/ExternalUserID/' + str(user_id)

headers = {'ContentType': 'application/json', 'ApiKey': api_key}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    if response.json()['Cleared'] == 'Yes':
        print('Transaction details:\n')
        print(json.dumps(response.json(), indent=4) + '\n')
    else: 
        print('\nUser ' + user_id + ' is not cleared to place requests.\n')
        sys.exit()
    

else:
    print('Transaction not found.')