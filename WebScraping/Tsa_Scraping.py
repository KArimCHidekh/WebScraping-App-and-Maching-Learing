
# Scrape website with IP protection and cloudflare protection
import cfscrape
import requests
import scraper as scraper
from bs4 import BeautifulSoup as soup, BeautifulSoup
import csv
import time



def get_proxies():
    # Find a free proxy provider website
    # Scrape the proxies
    proxy_web_site = 'https://free-proxy-list.net/'
    response = requests.get(proxy_web_site)
    page_html = response.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "table-responsive"})[0]
    ip_index = [8 * k for k in range(80)]
    proxies = set()

    for i in ip_index:
        ip = containers.find_all("td")[i].text
        port = containers.find_all("td")[i + 1].text
        https = containers.find_all("td")[i + 6].text
        print("\nip address : {}".format(ip))
        print("port : {}".format(port))
        print("https : {}".format(https))

        if https == 'yes':
            proxy = ip + ':' + port
            proxies.add(proxy)

    return proxies
# end get_proxies()


def check_proxies():
    # check the proxies and save the working ones
    proxies = get_proxies()
    test_url = 'https://httpbin.org/ip'
    for i in proxies:
        print("\nTrying to connect with proxy: {}".format(i))
        try:
            response = requests.get(test_url, proxies={"http": i, "https": i}, timeout=5)
            print("working proxy found")
            return i
            break
        except:
            print("Connnection error")
    return 0

# end check_proxies


url = "https://www.tsa-algerie.com/?fbclid=IwAR18ax7fmdJxtwhnJLt3id-7uSqtS-RQiDem2XiDNh5JRPYYBpHxvMFFDeI"
working_proxy = check_proxies()
if working_proxy != 0:
    scraper = cfscrape.create_scraper()
    proxies = {"http": working_proxy, "https": working_proxy}
    resp = scraper.get(url, proxies=proxies, allow_redirects=True, timeout=(10, 20))
    resp = resp.text
else:
    print ("no working proxy found")
soup = BeautifulSoup(resp,'html.parser')

#All the contents
main = soup.find('div',class_='ntdg__main ntdg__main--mcic')
atag = main.find_all('h2',class_='ntdga__title transition')
atag = atag[:10]


arti_link = []
arti_title = []

    

for t in atag:

    title = t.text.strip()
    link = t.find('a')['href']
    arti_title.append(title)
    arti_link.append(link)

    
Dz_Articles = pd.DataFrame(
    {
    'Titles' : article_title,
    'Links' : arti_link,
    #'Science' : temperatures,
    })

print(Dz_Articles)

Dz_Articles.to_csv('tsa.csv')
   
          
    