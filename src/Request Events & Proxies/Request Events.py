import requests


def get_status_text(r, *args, **kwargs):
    print(r.text)
    print(f"Your reason {r.reason} _ And your status code is : {r.status_code}")

def get_headers_cookies(r, *args, **kwargs):
    print(r.headers)
    print(r.cookies)

event_hook = {
    "response": [get_status_text, get_headers_cookies]

}


response = requests.get("https://github.com", hooks=event_hook)