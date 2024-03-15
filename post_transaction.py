import requests
from config import api_key, api_base

api_url = api_base + '/Transaction/'
headers = {'ContentType': 'application/json', 'ApiKey': api_key}
transaction = { # The data below is fake and is only used for demo purposes. You can replace it with your own data if you choose.
            'ExternalUserId': '', # Replace with the external user ID of the requester.
            'RequestType': 'Article',
            'ProcessType': 'Borrowing',
            'PhotoJournalTitle': 'Journal of the American Chemical Society',
            'PhotoArticleTitle': 'A New Class of Macrocyclic Host Molecules Possessing Two Different Types of Binding Site. Synthesis and Complexation Properties of Cyclic Tetraureas',
            'PhotoArticleAuthor': 'Cram, D. J.; Knobler, C. B.; Sauvage, J. P.',
            'PhotoJournalVolume': '93',
            'PhotoJournalIssue': '11',
            'PhotoJournalYear': '1971',
            'PhotoJournalInclusivePages': '2897-2899',
            'DOI': '10.1021/ja00741a041',
        }

response = requests.post(api_url, headers=headers, json=transaction)

if response.status_code == 200:
    print('Success!')
else:
    print(str(response.status_code) + ': ' + response.json()['Message'] + '\n')
