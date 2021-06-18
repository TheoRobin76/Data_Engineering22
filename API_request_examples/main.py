import json

import requests
from pprint import pprint #pretty print prints prettily

# post_code_req = requests.get("https://api.postcodes.io/postcodes/AL11HA")
#
# # print(post_code_req.status_code) #200 is good, 400 means error
# # pprint(post_code_req.headers) #info about the request
# pprint(post_code_req.json()) #looks much clearer to print dictionaries inside dictionaries

json_body = json.dumps({'postcodes': ['AL11HA', 'WD231NQ', 'WD63JW']}) #querying multiple postcodes
headers = {'Content-type': 'application/json'}

post_multi_req = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=json_body)
pprint(post_multi_req.json())




