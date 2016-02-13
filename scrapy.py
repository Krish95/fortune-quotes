from bs4 import BeautifulSoup

import requests

import re

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


url = "http://www.fortunecookiemessage.com"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

text = str(soup.find_all('a',class_='cookie-link'))

text = text.strip('[]')

print(striphtml(text))
