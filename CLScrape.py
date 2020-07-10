import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://richmond.craigslist.org/search/sss?query=vinyl+record&sort=rel'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='sortable-results')

vinyl_elems = results.find_all('li', class_= 'result-row')

for vinyl_elem in vinyl_elems:
    vinylTitle = vinyl_elem.find('a', class_='result-title')
    vinylPrice = vinyl_elem.find('span', class_='result-price')
    vinylLink = vinyl_elem.find('a')['href']
    print(vinylTitle.text,' ',vinylPrice.text)
    print(vinylLink+'\n')