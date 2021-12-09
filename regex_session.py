import re
import requests
from bs4 import BeautifulSoup


## Part 1
url = 'http://tolkiengateway.net/wiki/Poems_in_The_Lord_of_the_Rings'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
mc = soup.find('div', id='mainContent')
list_items = mc.find_all('a')
for record in list_items:
    if record.parent.name == 'li':
        print(record.text, record["href"])


## Part 2

# https://regex101.com/
# rap    NBAYOUNGBOAT    https://i.scdn.co/image/ab67616d0000b2732dd3f11b04f31d9acd49015b    Lil Yachty  139845  TRUE    6K2anECyrckidwf5wxS78Q  69  2018-03-09  day 17  0.769   0.807   11  -2.966  1   0.306   0.0515  0   0.111   0.364   82.422  4
# (https*.+?)\t

# (https*.+?)\t(.*?)\t

with open('spotify_genre.txt', 'r', encoding='utf-8') as f:
    file = f.read()


results = re.findall(r'(https*.+?)\t(.*?)\t', file)
for record in results:
    print(record[1], record[0])


## Part 3
#python regex_practice.py