import requests
from bs4 import BeautifulSoup
import time
#Create reviews dataframe

reviews1 = pd.read_csv("2008-01-01_to_2008-01-31.csv")
reviews2 = pd.read_csv("2008-02-01_to_2008-12-31.csv")
reviews3 = pd.read_csv("2009-01-01_to_2009-12-31.csv")
reviews4 = pd.read_csv("2010-01-01_to_2010-10-07.csv")
reviews5 = pd.read_csv("2010-10-08_to_2012-12-31.csv")
reviews6 = pd.read_csv("2013-01-01_to_2013-06-30.csv")
reviews7 = pd.read_csv("2013-07-01_to_2015-11-30.csv")
reviews8 = pd.read_csv("2015-12-01_to_2017-03-04.csv")

reviews = reviews_2 = reviews1.append(reviews2).append(reviews3).append(reviews4).append(reviews5).append(reviews6).append(reviews7).append(reviews8)

URL_List = reviews['url']
#Scrape review text
for URL in URL_List:
    r = requests.get(URL)
    html = r.text
    #Allow different formats for articles
    if BeautifulSoup(html, "lxml").find_all('p', {"itemprop":"articleBody"})!=[]:
        article = BeautifulSoup(html, "lxml").find_all('p', {"itemprop":"articleBody"})
    elif BeautifulSoup(html, "lxml").find_all('p', {"itemprop":"reviewBody"})!=[]:
        article = BeautifulSoup(html, "lxml").find_all('p', {"itemprop":"reviewBody"})
    elif BeautifulSoup(html, "lxml").find_all('p', {"class":"story-body-text story-content"})!=[]:
        article =BeautifulSoup(html, "lxml").find_all('p', {"class":"story-body-text story-content"})
    else:
        article =BeautifulSoup(html, "lxml").find_all('p')
    body = ["None"]*len(article)
    for i in range(0, len(article)):
        body[i]=article[i].get_text()
    text ="\n".join(body)
    #Append to existing dataframe
    reviews.loc[reviews.url==URL, 'text'] = text
    time.sleep(1)

reviews.to_csv("reviews.csv", na_rep=np.nan, index=False, encoding="utf-8")
