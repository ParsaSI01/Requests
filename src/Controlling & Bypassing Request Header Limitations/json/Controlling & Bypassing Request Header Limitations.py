import requests
import json

url = "https://api.divar.ir/v8/my-divar/web/menu"

with open("json/headers.json", "r", encoding="utf-8") as file:
    headers = json.load(file)

response = requests.post(url=url, headers=headers)

print(response.request.headers)
