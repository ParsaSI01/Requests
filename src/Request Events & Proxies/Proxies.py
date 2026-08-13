import json

import requests

with open("json/proxies.json", "r") as file:
    proxy = json.load(file)

response = requests.get("https://httpcan.org/ip", proxies=proxy)
print(response.text)