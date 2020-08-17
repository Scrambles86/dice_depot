from django.db import models
import requests
import os
import json

ENDPOINT = os.environ.get('ENDPOINT')
API_SECRET_KEY = os.environ.get('API_SECRET_KEY', '')
API_CLIENT_ID = os.environ.get('API_CLIENT_ID', '')


response = requests.get("https://api.boardgameatlas.com/api/search?client_id=yrOwuRj5mj")
data = response.json()

print(type(data))
print(data)

out_file = open("products/fixtures/products.json", "w")

json.dump(data, out_file)
