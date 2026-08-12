import requests

import json

# ====================
# GET method
# ====================

with open("json/parametrs.json", "r", encoding="utf-8") as file:
    parametrs = json.load(file)

response = requests.get(
    "https://httpcan.org/get",
    params=parametrs
)

# print(response.status_code)

# print(response.url)

# print(response.text)

with open("json/get.json", "w", encoding="utf-8") as file:
    json.dump(response.json(), file, indent=4)

with open("json/get.json", "r", encoding="utf-8") as file:
    get_response = file.read()

print(get_response)

# ====================
# POST Method
# ====================

with open("json/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# data = [("username", "sajad"), ("password", 1234)]

response2 = requests.post(
    url="https://httpcan.org/post",
    data=data
)

# print(response2.status_code)

# print(response2.url)

# print(response2.text)

with open("json/post.json", "w", encoding="utf-8") as file:
    json.dump(response2.json(), file, indent=4)

with open("json/post.json", "r", encoding="utf-8") as file:
    post_response = file.read()

print(post_response)