#!/usr/bin/env python3
# get_transaction.py
# Description: A demo script that returns details about an ILLiad transaction using ILLiad Web Services.
# Author: Kristen Wilson, NC State Libraries, kmblake@ncsu.edu

import requests
import json
from config import api_key, api_base

transaction_id = '000' # Replace with the transaction ID you want to get details for.
api_url = api_base + '/Transaction/' + str(transaction_id)

headers = {'ContentType': 'application/json', 'ApiKey': api_key}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    print('Transaction details:\n')
    print(json.dumps(response.json(), indent=4) + '\n')
else:
    print(str(response.status_code) + ': ' + response.text)