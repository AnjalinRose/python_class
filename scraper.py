import requests 
from bs4 import BeautifulSoup
URL="https://www.cet.ac.in/head-of-departments/"
req=requests.get(URL)
source_code = req.content

soup=BeautifulSoup(source_code,'lxml')
table=soup.find('table')
rows=table.find_all('tr')
rows= rows [1:]
for row in rows:
    columns=row.find_all('td')
    hod_name= columns[0].text
    dept=columns[1].text
    number=columns[2].text
    print(hod_name,dept,number)
