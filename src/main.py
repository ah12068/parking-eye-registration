import requests as r
from os import environ

# post reg-plate to the form
payload = {"Plate": environ['reg-plate']}
response = r.post(environ['parking-url'], data=payload)
print(response.status_code)