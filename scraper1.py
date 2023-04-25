import requests 
from bs4 import BeautifulSoup
URL="http://books.toscrape.com/"
req=requests.get(URL)
source_code = req.content

soup=BeautifulSoup(source_code,'lxml')
title=soup.find_all('article')
for i in title
titles=title.find_all('h3')
for title in titles:
    print(title.text)
