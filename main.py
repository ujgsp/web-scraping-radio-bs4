import requests
import csv
from bs4 import BeautifulSoup

URL = "https://www.radio-en-vivo.mx/"

page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

sidebar = soup.find(id="collapse_2")
links = sidebar.find_all('a', class_="mdc-button mdc-button--raised mdc-button--primary radio-filter-button mdc-typography--caption")

# store to new list data
city = []

# csv: set header for csv file
headers = ['Radio_names', 'City_names','Radio_urls', 'Image_urls']


for data in links:
    link = data.get('href') # /radio/aguascalientes

    CITYNAME = data.get_text().strip()

    url_city = "https://www.radio-en-vivo.mx" + link
    page_city = requests.get(url_city)

    soup_city = BeautifulSoup(page_city.text, "html.parser")

    # print(CITYNAME)

    # content data
    result = soup_city.find('div', class_='mdc-grid-list')

    contents = result.find_all('li', class_='mdc-grid-tile')
    for content in contents:
        RADIONAME = content.find('span', class_='mdc-grid-tile__title').get_text().strip()
        RADIOURL = content.find('a').get('href').strip()
        RADIOURL = "https://www.radio-en-vivo.mx" + RADIOURL
        IMG = content.find("img", attrs={"data-src": True})
        if IMG:
            IMG = IMG.get("data-src")
        else:
            # IMG = None
            IMG = content.find('img').get('src').strip()

        # city.append([RADIONAME.encode('utf-8'), CITYNAME.encode('utf-8'), RADIOURL.encode('utf-8'), IMG.encode('utf-8')])
        city.append([RADIONAME, CITYNAME, RADIOURL, IMG])

        # print("Nama Radio: " + RADIONAME + " Nama Kota: " + CITYNAME + "| URL: " + RADIOURL + " | IMG URL: " + IMG)

# csv: write csv file
with open('main_radio_by_kota.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # write header
    writer.writerow(headers)
    # write city
    writer.writerows(city)