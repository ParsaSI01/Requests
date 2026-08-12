import json
import sqlite3

import requests

with open("../json/json/headers.json", "r", encoding="utf-8") as file:
    headers = json.load(file)

connection = sqlite3.connect("sql/database.db")
cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS headers
               (
                   key
                   TEXT
                   UNIQUE,
                   value
                   TEXT
               )
               """)

cursor.execute("DELETE FROM headers")

for key, value in headers.items():
    cursor.execute(
        "INSERT INTO headers (key, value) VALUES (?, ?)",
        (key, value)
    )

connection.commit()


cursor.execute("SELECT key, value FROM headers")

headers = dict(cursor.fetchall())

url = "https://api.divar.ir/v8/my-divar/web/menu"

response = requests.post(
    url=url,
    headers=headers
)

print(response.request.headers)

connection.close()
