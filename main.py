import requests
from bs4 import BeautifulSoup

URL = "https://www.radio-en-vivo.mx/"

page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

sidebar = soup.find(id="collapse_2")

print(sidebar)