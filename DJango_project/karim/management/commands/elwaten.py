from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
#import pandas as pd

from karim.models import  Article


class Command(BaseCommand):
    help = 'Poling articles from elwaten'

    #ef add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        aa="hello mala"
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % aa))
        '''
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        '''

        page = requests.get('https://www.elwatan.com/')
        soup = BeautifulSoup(page.content, 'lxml')
        # week = soup.find(class_ ='vc_row wpb_row vc_row-fluid container vc_custom_1510226780605')
        sections = soup.find_all(class_='wpb_wrapper')
        #print("Section count : " + str(len(sections)))

        article_data = list()

        i = 1
        for section in sections:

            sectiontitle = section.find('a')
            sectiontitletxt = "NON"
            if sectiontitle:
                sectiontitletxt = str(sectiontitle.getText()).strip()

            articles = section.find_all('article')
            articlescount = len(articles)
            if articlescount > 0 and sectiontitletxt != "NON" and sectiontitletxt != "":
                #print("--- Section id : " + str(
                #    i) + "----------------------------------------------------------------------------------------")
                #print("\tSection title : " + sectiontitletxt)
                #print("\tArticle count : " + str(articlescount))
                ii = 1
                for tag_article in articles:

                    #print("\t\t-- Article id : " + str(ii))
                    article = dict()
                    title = "***"
                    link = "***"
                    title = tag_article.find_all('a', href=True)[0].text

                    link = tag_article.find_all('a', href=True)[0]['href']

                    if not title.strip():
                        tt = tag_article.find_all('a', href=True)
                        if (len(tt) > 1):
                            title = tt[1].text
                            link = tt[1]['href']
                    """
                    if ii == 1 :
                        tt=tag_article.find_all('a',href=True)
                        if(len(tt)>1):
                            title  = tt[1].text
                            link   = tt[1]['href']
                    """
                    title = title
                    print("\t\tTitle : " + title)
                    print("\t\tLink: " + link)
                    # article["data"]= str(tag_article)
                    article["category"] = sectiontitletxt
                    article["title"] = title
                    article["link"] = link

                    #----
                    art = Article()
                    art.title=article["title"]
                    art.link=article["link"]
                    art.tag=article["category"]
                    art.source="EL-WATEN"
                    #art.date_save=timezone.now()

                    num_results = Article.objects.filter(title=art.title).count()
                    if num_results <= 0 :
                        art.save()
                        self.stdout.write(self.style.SUCCESS('Article saving : "%s"' % art.title))
                    else :
                        self.stdout.write(self.style.SUCCESS('Article Already exist : "%s"' % art.title))
                    #----
                    article_data.append(article)
                    ii = ii + 1

                i = i + 1

        #data = pd.DataFrame(article_data)