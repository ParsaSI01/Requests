import requests
import json

url = "https://www.amazon.com"

with open("json/headers2.json", "r", encoding="utf-8") as file:
    headers = json.load(file)

response = requests.get(url=url, headers=headers)

print(response.request.headers)
