import requests
import json
import sqlite3


with open("../json/json/headers2.json", "r", encoding="utf-8") as file:
    headers = json.load(file)


connection = sqlite3.connect("sql/database.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS headers (
        key TEXT UNIQUE,
        value TEXT
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



url = "https://www.amazon.com"

response = requests.get(
    url=url,
    headers=headers
)

print(response.request.headers)

connection.close()