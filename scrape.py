
import urllib.request
from bs4 import BeautifulSoup
import re

url = 'http://www.hearthstonetopdecks.com/card-category/set/expansions/the-witchwood/'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

# string = String(soup)
# print(soup)

# Yep this is what we want:
result = soup.find_all('strong')


result = soup.find_all('img')

for r in result:
    # print(r)
    string = str(r)
    print(string, '\n')
    ind = 1000
    if 'png' in string:
        ind = string.index('png')
    elif 'gif' in string:
        ind = string.index('gif')
    elif 'png' in string:
        ind = string.index('png')
    print(string[string.index('src'): ind])
