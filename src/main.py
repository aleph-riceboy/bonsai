# Bonsai
# A cli cryptocurrency price tracker

import requests
import json
#from crypto_list import list

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://api.coingecko.com/api/v3/coins/dogecoin")

jprint(response.json())
