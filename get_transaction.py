import requests
import json
from config import api_key, api_base

transaction_id = 0 # Replace with the transaction ID you want to get details for.
api_url = api_base + '/Transaction/' + str(transaction_id)

headers = {'ContentType': 'application/json', 'ApiKey': api_key}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    print('Transaction details:\n')
    print(json.dumps(response.json(), indent=4) + '\n')
else:
    print('Transaction not found.')