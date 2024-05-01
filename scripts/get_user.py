#!/usr/bin/env python3
# get_user.py
# Description: A demo script that checks an ILLiad user's status and returns user details using the ILLiad Web Platform.
# Author: Kristen Wilson, NC State Libraries, kmblake@ncsu.edu

import requests
import json
from config import api_key, api_base

user_id = 'xxx@yourschool.edu' # Enter the external user ID here
api_url = api_base + '/Users/ExternalUserID/' + str(user_id)

headers = {'ContentType': 'application/json', 'ApiKey': api_key}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    if response.json()['Cleared'] == 'Yes':
        print('Transaction details:\n')
        print(json.dumps(response.json(), indent=4) + '\n')
    else: 
        print('\nUser ' + user_id + ' is not cleared to place requests.\n')    

else:
    print(str(response.status_code) + ': ' + response.json()['Message'] + '\n')