import json
import sqlite3
import requests

# ====================
# GET method
# ====================

connection = sqlite3.connect("sql/database.db")
cursor = connection.cursor()

with open("../json/json/parametrs.json", "r", encoding="utf-8") as file:
    parameters = json.load(file)

cursor.execute("""
CREATE TABLE IF NOT EXISTS parameters (
    key TEXT UNIQUE,
    value TEXT
)
""")

cursor.execute("DELETE FROM parameters")

for key, value in parameters.items():
    if isinstance(value, list):
        value = json.dumps(value)

    cursor.execute(
        "INSERT OR REPLACE INTO parameters (key, value) VALUES (?, ?)",
        (key, str(value))
    )

cursor.execute("SELECT key, value FROM parameters")

parameters = {}

for key, value in cursor.fetchall():
    try:
        parameters[key] = json.loads(value)
    except json.JSONDecodeError:
        parameters[key] = value

response = requests.get(
    "https://httpcan.org/get",
    params=parameters
)

# print(response.status_code)

# print(response.url)

# print(response.text)

cursor.execute("""
CREATE TABLE IF NOT EXISTS get_responses (
    response TEXT
)
""")

cursor.execute("DELETE FROM get_responses")

cursor.execute(
    "INSERT INTO get_responses (response) VALUES (?)",
    (response.text,)
)

get_response = cursor.execute(
    "SELECT response FROM get_responses"
).fetchone()[0]

print(json.dumps(json.loads(get_response), indent=4))

connection.commit()

# ====================
# POST Method
# ====================

with open("../json/json/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

cursor.execute("""
CREATE TABLE IF NOT EXISTS post_data (
    key TEXT UNIQUE,
    value TEXT
)
""")

cursor.execute("DELETE FROM post_data")

for key, value in data.items():
    cursor.execute(
        "INSERT OR REPLACE INTO post_data (key, value) VALUES (?, ?)",
        (key, str(value))
    )

cursor.execute("SELECT key, value FROM post_data")

data = dict(cursor.fetchall())


response2 = requests.post(
    "https://httpcan.org/post",
    data=data
)

# print(response2.status_code)

# print(response2.url)

# print(response2.text)

cursor.execute("""
CREATE TABLE IF NOT EXISTS post_responses (
    response TEXT
)
""")

cursor.execute("DELETE FROM post_responses")

cursor.execute(
    "INSERT INTO post_responses (response) VALUES (?)",
    (response2.text,)
)

post_response = cursor.execute(
    "SELECT response FROM post_responses"
).fetchone()[0]

print(json.dumps(json.loads(post_response), indent=4))

connection.commit()

connection.close()