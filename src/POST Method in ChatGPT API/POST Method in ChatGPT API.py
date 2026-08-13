import json
import requests

url = "https://api.openai.com/v1/chat/completions"


with open("json/headers.json", "r") as file:
    headers = json.load(file)

with open("json/data.json", "r") as file:
    data = json.load(file)

response = requests.post(url=url, headers=headers, json=data)

print(response.status_code)