import datetime
from nltk import tokenize
import pandas as pd
#Make author/title lists for reference

lists_2016 = pd.read_csv("2016-01-03_to_2017-01-29.csv", na_values="NaN")
lists_2012_2015 = pd.read_csv("2012-01-01_to_2015-12-27.csv", na_values="NaN")
lists_2008_2009 = pd.read_csv("2008-06-08_to_2009-06-21.csv", na_values="NaN")
lists_2009_2011 = pd.read_csv("2009-06-28_to_2011-12-25.csv", na_values="NaN")
lists_leftover = pd.read_csv("leftovers.csv", na_values="NaN")

lists_new = lists_2009_2011.append(lists_leftover)
lists_work = lists_2008_2009.append(lists_2012_2015).append(lists_2016)
lists_final = lists_work.append(lists_new)

author_list = lists_final.groupby("author").agg("count").iloc[:,0].sort_values(ascending=False)
title_list = lists_final.groupby(["author", "title"]).agg("count").iloc[:,0].sort_values(ascending=False)
#Add in parent/genre columns
publisher = pd.merge(pd.DataFrame(corp_owner.values(), corp_owner.keys()), pd.DataFrame(genre.values(), genre.keys()), how = "outer", left_index=True, right_index=True)
publisher.columns= ['parent', 'genre']
publisher.index = publisher.index.str.upper()
list_pub = pd.merge(lists_final, publisher, left_on='publisher', right_index=True, how="outer")

#Deal with null values
list_pub['parent'][list_pub['parent'].isnull()] = "Small Imprint"
list_pub['genre'][list_pub['genre'].isnull()] = "Small Imprint"

#Convert list dates to standard datetime values
def convert_date(x):
    x= str(x)
    if x.find("/") > -1:
        return datetime.datetime.strptime(x, "%m/%d/%Y").date()
    else:
        try:
            return datetime.datetime.strptime(x, "%Y-%m-%d").date()
        except:
            return (x)

list_pub['published_date']=list_pub['published_date'].apply(convert_date)
#Get rid of weird null rows
list_pub = list_pub.dropna(thresh=5)
#Generate year column
list_pub['year']=[x.year for x in list_pub['published_date']]
#Deal with the Great Merger
list_pub['parent'][(list_pub.published_date>datetime.date(2013, 7, 12)) & ((list_pub.parent=='Penguin')\
                                                                           | (list_pub.parent=="Random House"))]="Penguin Random"
#Tokenize sentences to export and hand-annotate
for review in reviews['text']:
    text =  tokenize.sent_tokenize(review.decode('utf-8'))
    for sentence in text:
        review_sent = open('reviews_text.txt', 'a')
        review_sent.write(sentence.encode('utf-8'))
        review_sent.write("\n")
        review_sent.close()
