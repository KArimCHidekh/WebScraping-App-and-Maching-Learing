import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get( 'https://www.liberte-algerie.com/')
soup = BeautifulSoup(page.content, 'html.parser')

page = soup.find(id= "bottom-posts")

k = page.find_all('a')

linkp = list ()
article_t =list()

for a in k: 

    titles = format(a.text)
    
    links = format(a.get("href"))

    linkp.append(links)
    article_t.append(titles)




Dz_Articles = pd.DataFrame(
	{
	'Titles' : article_t,
	'Links' : linkp,
	
	})

print(Dz_Articles)

