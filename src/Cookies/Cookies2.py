import json
import requests


response = requests.get("https://github.com", timeout=20)




with open("json/cookies2.json", "w") as file:
    json.dump(response.cookies.get_dict(),file , indent=4)


with open("json/cookies2.json", "r") as file:
    cookies = json.load(file)


copy_cookies = cookies.copy()
cookies2 = cookies


print(copy_cookies)
print(cookies)
