import json
import requests

with open("json/cookies.json", "r") as file:
    cookies = json.load(file)

jar = requests.cookies.RequestsCookieJar()

jar.set("item1", "value1", domain="httpcan.org", path="/cookies")


response = requests.get("https://httpcan.org/cookies", cookies= jar)

print(response.text)
print(response.request.headers)
