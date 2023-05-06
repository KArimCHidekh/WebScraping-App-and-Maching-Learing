import requests
from bs4 import BeautifulSoup
import csv
import time

req = requests.get('https://www.liberte-algerie.com/?fbclid=IwAR1Nm3q72m8gF-uqQARnwxVOXx3mBTbgaOugvmKUa-Je0-u5aHKfvoVzeEE')
soup = BeautifulSoup(req.text,'html.parser')

#All the contents
main = soup.find('div',id='contenu')

#Some a tags have differnt classes so...
atag = main.find_all('a',class_='title')
atag = atag[:10]

arti_link = []
arti_title = []

while True:
    l = 0
    for t in atag:
        title = t.text.strip()
        link = '  https://www.liberte-algerie.com/actualite'+t['href']
        if title not in arti_title:
            arti_title.append(title)
        if link not in arti_link:
            arti_link.append(link)
        print(title)
        print(link)
        print()
        #Csv part
        with open('liberté.csv','w',newline='',encoding='utf-8') as l2:
            fieldnames = ['Article_Titles','Article_links']
            thewriter = csv.DictWriter(l2,fieldnames=fieldnames)

            thewriter.writeheader()
            for i in arti_title:
                thewriter.writerow({'Article_Titles':i,'Article_links':arti_link[l]})
            l+=1
    time.sleep(180)

        

    

        
    


































	


