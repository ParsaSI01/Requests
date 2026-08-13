import requests
from database import Database

url = 'https://api.divar.ir/v8/web-search/4/cars'

header = {'Content-Type': 'application/json'}

data = {'page': 1, 'json_schema': {'category': {'value': "cars"}}, 'last-post-date': 1716185835776001}

response = requests.post(url, headers=header, json=data)

next_last_post_date = response.json()['last_post_date']
widgets = response.json()['web_widgets']['post_list']


divar_db=Database('divar.db')

for item in widgets:
    car_detail_data = item['data']
    title = car_detail_data['title']
    kilometter = car_detail_data['top_description_text']
    price = car_detail_data['middle_description_text']
    location = car_detail_data['bottom_description_text']
    detail_url=f'https://divar.ir/v/{title}/{car_detail_data['token']}'
    divar_db.insert_into_db(title,kilometter,price,location,detail_url)




