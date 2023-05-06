import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

req = requests.get('http://www.aps.dz/algerie')
soup = BeautifulSoup(req.text,'html.parser')
main = soup.find('div',id='itemListLeading')
atag = main.find_all('h3',class_='catItemTitle')

arti_link = []
arti_title = []
while True:
    for i in atag:
        link = (i.find('a')['href'])
        title = (i.text).strip()
        if title not in arti_title:
            arti_title.append(title)
        if link not in arti_link:
            arti_link.append(link)
        print("the title is :  "+title)
        print("the link is :  "+link)
        print()
    l = 0
     #CSV part
    with open('aps.csv','w',newline='') as l1:
        fieldnames = ['Article_Titles','Article_links']
        thewriter = csv.DictWriter(l1,fieldnames=fieldnames)

        thewriter.writeheader()
        for i in arti_title:
            thewriter.writerow({'Article_Titles':i,'Article_links':arti_link[l]})
            l+=1
    time.sleep(180)