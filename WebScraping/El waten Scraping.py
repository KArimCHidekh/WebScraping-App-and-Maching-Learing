
import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get( 'https://www.elwatan.com/')
soup = BeautifulSoup(page.content, 'lxml')
#week = soup.find(class_ ='vc_row wpb_row vc_row-fluid container vc_custom_1510226780605')
sections = soup.find_all(class_ ='wpb_wrapper')
print ("Section count : " +str(len(sections)))


article_data =list()

i= 1
for section in sections:

    sectiontitle = section.find('a')
    sectiontitletxt ="NON"
    if sectiontitle :
         sectiontitletxt=str(sectiontitle.getText()).strip()

         
    articles = section.find_all('article')
    articlescount = len(articles)
    if articlescount > 0 and sectiontitletxt != "NON" and sectiontitletxt != "" :
        print ("--- Section id : "+str(i)+"----------------------------------------------------------------------------------------")  
        print ("\tSection title : "+sectiontitletxt)
        print ("\tArticle count : " +str(articlescount))
        ii=1
        for tag_article in articles:
            
            print ("\t\t-- Article id : "+str(ii))
            article = dict()
            title="***"
            link="***" 
            title  = tag_article.find_all('a',href=True)[0].text
            
            link   = tag_article.find_all('a',href=True)[0]['href']
            
            if not title.strip():
                tt=tag_article.find_all('a',href=True)
                if(len(tt)>1):
                    title  = tt[1].text
                    link   = tt[1]['href']
            """
            if ii == 1 :
                tt=tag_article.find_all('a',href=True)
                if(len(tt)>1):
                    title  = tt[1].text
                    link   = tt[1]['href']
            """   
            title = title
            print ("\t\tTitle : " +title)
            print ("\t\tLink: " +link)
            #article["data"]= str(tag_article)
            article["category"]= sectiontitletxt
            article["title"]= title
            article["link"]=link
            article_data.append(article)
            ii=ii+1

        i=i+1

data = pd.DataFrame(article_data)
#data.to_csv(r'D:\KARIm.csv',index=False)



