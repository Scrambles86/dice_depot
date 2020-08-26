#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.db import models
import requests
import json


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dice_depot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# API Json Import

#ENDPOINT = os.environ.get('ENDPOINT')
#API_SECRET_KEY = os.environ.get('API_SECRET_KEY', '')
#API_CLIENT_ID = os.environ.get('API_CLIENT_ID', '')


#response = requests.get("https://api.boardgameatlas.com/api/search?client_id=yrOwuRj5mj")
#data = response.json()

#print(type(data))
#print(data)

#out_file = open("products/fixtures/products_full.json", "w")

#json.dump(data, out_file)

