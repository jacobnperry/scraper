import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://auction.ebidlocal.com/cgi-bin/mmlist.cgi?staples406/category/ALL'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div',id='SelectCat')
nextResults = results.find('td', class_='listrefresh')
nextNext = nextResults.find('input', {'name': "searchcount"})
totalCount = nextNext.get('value')
baseURL = URL[:-12]
i = 1
itemURL = baseURL + str(i)
itemSource = requests.get(itemURL)




while i <= int(totalCount):
    itemURL = baseURL + str(i)
    itemSource = requests.get(itemURL)
    itemSoup = BeautifulSoup(itemSource.content, 'html.parser')
    itemDescription = itemSoup.find('td', class_='description')
    if 'musical' in itemDescription.text.lower():
        print(itemDescription.text.lower())
#    print(itemDescription.text)
    i= i + 1









