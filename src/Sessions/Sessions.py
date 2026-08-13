import json
import requests


with open("json/user.json") as file:
    data = json.load(file)
    user = data["user"]
    ip = data["ip"]
    del data

with open("json/headers.json") as file:
    headers = json.load(file)


with open("json/headers2.json") as file:
    headers2 = json.load(file)




get_cookies_url = "https://httpcan.org/cookies"
set_cookies_url = "https://httpcan.org/cookies/set"

session = requests.Session()

session.headers.update(headers)

# with requests.Session() as s:
#     s.get(get_cookies_url)


session.get(set_cookies_url, params=user)
session.get(set_cookies_url, params=ip)

response = session.get(get_cookies_url)

print(response.text)
print(response.request.headers)

print(response.cookies)