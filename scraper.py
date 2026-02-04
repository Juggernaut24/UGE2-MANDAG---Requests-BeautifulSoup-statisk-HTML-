import requests
from bs4 import BeautifulSoup
import json
import os

os.makedirs('outputs', exist_ok = True)

target_url = "https://quotes.toscrape.com/"

response = requests.get(target_url)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

#print(response.content)

print(soup)