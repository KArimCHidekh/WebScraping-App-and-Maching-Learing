
import requests
from bs4 import BeautifulSoup

import csv
import time
import locale
import datetime
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
'fr_FR.UTF-8'
from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
#import pandas as pd

from karim.models import  Article


def parse_date(date_txt):
    DATE_FORMAT = "%A, %d %B %Y %H:%M"
    return datetime.datetime.strptime(date_txt, DATE_FORMAT)




class Command(BaseCommand):
    help = 'Poling articles from APS'

    #ef add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        aa="staring"
        self.stdout.write(self.style.SUCCESS('Poling articles from APS "%s"' % aa))


        categories =["sante-science-technologie" ,"regions" ,"culture" ,"societe" ,"sport" ,"monde" ,"economie" ,"algerie"]
        source ='http://www.aps.dz'
        pages =6

        for category in  categories:
            tag =category
            req = requests.get(source +"/" +category)

            soup = BeautifulSoup(req.text ,'html.parser')
            aaa= soup.find('div' ,class_='k2Pagination')

            total_pages= aaa.text[-5:].strip()



            ii =0
            for page in range(1 ,pages):
                print ("---------------- Page: %d " %page)
                sub_req = requests.get('http://www.aps.dz/'+category+'/?start= ' +str(ii))
                sub_soup = BeautifulSoup(sub_req.text ,'html.parser')
                jj =1
                for article in sub_soup.find_all('div' ,class_='itemContainer'):
                    print ("----------Article: %d " %jj)
                    tag_title= article.find('h3' ,class_='catItemTitle').find("a", recursive=False)
                    title =tag_title.text
                    link = source+tag_title['href']
                    intro   = article.find('div' ,class_="catItemIntroText").text.strip()
                    pub_date =article.find('span' ,class_="catItemDateCreated").text.strip()



                    print("\t\tTitle: %s " %title)
                    print("\t\tIntro: %s " %intro)
                    print("\t\tLink : %s " %link)
                    print("\t\tDate :  " +str(parse_date(pub_date)))
                    print("\t\tTag: %s " %tag)
                    print("\t\tSource: %s " %source)

                    print()
                    jj =jj +1

                    art = Article()
                    art.title = title
                    art.intro= intro
                    art.link = link
                    art.tag = tag
                    art.source = source
                    art.date_pub=parse_date(pub_date)

                    num_results = Article.objects.filter(title=art.title).count()
                    if num_results <= 0:
                        art.save()
                        self.stdout.write(self.style.SUCCESS('Article saving : "%s"' % art.title))
                    else:
                        self.stdout.write(self.style.SUCCESS('Article Already exist : "%s"' % art.title))
                    # ----


                ii=ii+10
