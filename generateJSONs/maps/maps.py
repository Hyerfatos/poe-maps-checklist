# from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

"""
Create a json file with all maps
"""

# mapsPage = urlopen('https://pathofexile.gamepedia.com/Map').read()

maps = {
        'Unique': [],
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
        '10': [],
        '11': [],
        '12': [],
        '13': [],
        '14': [],
        '15': [],
        '16': [],
    }

with open('mapstable.html', encoding="utf8") as f:
    soup = BeautifulSoup(f, 'html.parser')

# Get all maps
titles = soup.find_all('tr')

for title in titles:
    td = title.find_all('td')

    tier = td[2].get_text().strip()
    if tier == 'N/A':
        continue

    href = td[0].find('a', href=True)
    name = href.get_text()
    url = 'https://pathofexile.gamepedia.com' + href['href']
    unique = td[3].find('img')['title']

    if unique.lower() == 'yes':
        tier = "Unique"

    maps[tier].append({'Name': name, 'Url': url})

with open('maps.json', 'w') as outfile:
    json.dump(maps, outfile, indent=4)
