import requests

import json

with open("json/parametrs.json", "r", encoding="utf-8") as file:
    parametrs = json.load(file)

with open("json/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

url = "https://api.divar.ir/v8/web-search/4/cars"
response = requests.post(url=url, params=parametrs, data=data)

with open("json/response.json", "w", encoding="utf-8") as file:
    json.dump(response.json(), file, indent=4)

with open("json/response.json", "r", encoding="utf-8") as file:
    widgets = json.load(file)

widgets = widgets["widget_list"][0]["data"]

for item in widgets:
    title = item
    print(title)