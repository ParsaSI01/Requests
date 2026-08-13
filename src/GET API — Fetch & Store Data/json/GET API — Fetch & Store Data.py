import json
import requests

csv_columns = ["title", "price", "image_url", "course_url", "courseLevel", "category"]


with open("json/parametrs.json", "r", encoding="utf-8") as file:
    parametrs = json.load(file)

url = "https://api.codeyad.com/api/course/getByFilter"

courses = []
page = 1

while True:
    parametrs["pageId"] = page

    response = requests.get(url=url, params=parametrs)
    response.raise_for_status()

    data = response.json()

    for item in data["data"]["data"]:
        courses.append({
            "title": item["courseTitle"],
            "price": item["price"],
            "image_url": f"https://codeyad.com/_ipx/w_600&f_webp&q_90&fit_contain/codeyad/assets/images/Courses/{item['imageName']}",
            "course_url": f"https://codeyad.com/Courses/{item['slug']}",
            "courseLevel": item["courseLevel"],
            "category": item["categoryTitle"]
        })

    if page >= data["data"]["pageCount"]:
        break

    page += 1

with open("json/courses.json", "w", encoding="utf-8") as file:
    json.dump(courses, file, indent=4, ensure_ascii=False)

