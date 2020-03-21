import requests
import json

from requests import Response

url = "https://www.cbr-xml-daIly.ru/daily_json.js"
response = requests.get(url)
data = json.loads(response.text)
print(data)