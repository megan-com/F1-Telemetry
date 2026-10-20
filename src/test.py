import requests

r = requests.get(
    "https://livetiming.formula1.com/static/"
)

print(r.status_code)