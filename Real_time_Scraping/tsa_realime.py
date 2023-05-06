
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


url = "https://www.tsa-algerie.com/"
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

while True:
    l = 0
    for t in atag:
        title = t.text.strip()
        link = t.find('a')['href']


        if title not in arti_title:
            arti_title.append(title)
        if link not in arti_link:
            arti_link.append(link)
        print(title)
        print(link)
        print()
        #Csv part
        with open('link3.csv','w',newline='',encoding='utf-8') as l2:
            fieldnames = ['Article_Titles','Article_links']
            thewriter = csv.DictWriter(l2,fieldnames=fieldnames)

            thewriter.writeheader()
            for i in arti_title:
                thewriter.writerow({'Article_Titles':i,'Article_links':arti_link[l]})
            l+=1
    time.sleep(180)
