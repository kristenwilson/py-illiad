#!/usr/bin/env python3
# put_transaction.py
# Description: A demo script that updates the status of an ILLiad transaction using the ILLiad Web Platform.
# Author: Kristen Wilson, NC State Libraries, kmblake@ncsu.edu

import requests
import json
from config import api_key, api_base

# Define the parameters for the request.
transaction_id = '000' # Replace with the transaction ID you want to cancel.
status = { "Status" : "Cancelled by ILL Staff" } # Replace with the status you want to set.

# Define the API endpoint and headers.
api_url = api_base + f'/transaction/{transaction_id}/route'
headers = {'ContentType': 'application/json', 'ApiKey': api_key}

# Send the request and check the response status code.
response = requests.put(api_url, headers=headers, json=status)
if response.status_code == 200:
    print('Transaction details: \n')
    print(json.dumps(response.json(), indent=4) + '\n')
else:
    print(str(response.status_code) + ': ' + response.json()['Message'] + '\n')