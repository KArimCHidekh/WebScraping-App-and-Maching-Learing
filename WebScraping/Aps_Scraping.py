import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

req = requests.get('http://www.aps.dz/sport')


soup = BeautifulSoup(req.text,'html.parser')
main = soup.find('div',id='itemListLeading')
atag = main.find_all('h3',class_='catItemTitle')

linkp_aps = list ()
article_aps =list()

for i in atag:

    link = (i.find('a')['href'])
    title = (i.text).strip()
    if title not in article_aps:
        article_aps.append(title)
    if link not in linkp_aps:
        linkp_aps.append(link)
       
     #CSV part
   
   

#CSV part

Dz_Article = pd.DataFrame(
    {
    'Titles' : article_aps,
    'Links' : linkp_aps,
    })

print(Dz_Article)

