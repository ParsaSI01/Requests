import csv
import json
import requests

URL = "https://api.codeyad.com/api/course/getByFilter"

CSV_COLUMNS = [
    "title",
    "price",
    "image_url",
    "course_url",
    "courseLevel",
    "category",
]

with open("json/parametrs.json", "r", encoding="utf-8") as file:
    parameters = json.load(file)

courses = []
page = 1

while True:
    parameters["pageId"] = page

    response = requests.get(URL, params=parameters)
    response.raise_for_status()

    data = response.json()
    page_data = data["data"]

    for item in page_data["data"]:
        courses.append({
            "title": item["courseTitle"],
            "price": item["price"],
            "image_url": (
                "https://codeyad.com/_ipx/w_600&f_webp&q_90&fit_contain/"
                f"codeyad/assets/images/Courses/{item['imageName']}"
            ),
            "course_url": f"https://codeyad.com/Courses/{item['slug']}",
            "courseLevel": item["courseLevel"],
            "category": item["categoryTitle"],
        })

    print(f"Page {page}/{page_data['pageCount']}")

    if page >= page_data["pageCount"]:
        break

    page += 1

with open(
    "csv/courses.csv",
    "w",
    encoding="utf-8-sig",
    newline=""
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=CSV_COLUMNS,
        quoting=csv.QUOTE_MINIMAL
    )

    writer.writeheader()
    writer.writerows(courses)

print(f"\nSaved {len(courses)} courses to csv/courses.csv")