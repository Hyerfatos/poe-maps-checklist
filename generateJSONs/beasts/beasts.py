# from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import collections

"""
Create a json file with all maps
"""
# Read html
with open('beasts.html', encoding="utf8") as f:
    soup = BeautifulSoup(f, 'html.parser')

# Initialise dictionary
beasts = collections.defaultdict(dict)
    
# Get all maps
beastsList = soup.find(id='displayTableK2X6b8Mrsa')
beastsList = beastsList.find_all(role='row')[1:]

# Loop to find all beasts
for beast in beastsList:
    td = beast.find_all('td')
	
    name = td[0].find('a', href=True).get_text()
    url = td[0].find('a', href=True)['href']
    genus = td[1].get_text()
    group = td[2].get_text()
    family = td[3].get_text()

    beasts.setdefault(family, collections.defaultdict(dict))
    beasts[family].setdefault(group, collections.defaultdict(list))
    beasts[family][group][genus].append({'name': name, 'url': url})

# Write json
with open('beasts.json', 'w') as outfile:
    json.dump(beasts, outfile, indent=4)
