import json
import pycurl
import pandas as pd
import numpy as np
from StringIO import StringIO
from api import NYT_API

#Get set of bestseller author names
author_list = pd.read_csv("author_list.csv", index_col=0, header=None)
full_reviews = pd.DataFrame()

#Request author range
print "What author # do you want to start with?"
author_start = int(raw_input('>'))
print "What author # do you want to end with?"
author_end = int(raw_input('>'))
authors = author_list.index.values[author_start:author_end].tolist()

csv_name = str(authors[0]) + "_to_" + str(authors[-1])+ ".csv"
#Request author reviews from API
for author in authors:
    name = "%20".join(author.split(" "))

    current_URL = "http://api.nytimes.com/svc/books/v3/reviews.json?author=%s&api-key=%s" %(name, NYT_API)
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, current_URL)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    current_reviews = buffer.getvalue()
    try:
        dict_reviews = json.loads(current_reviews)
        if dict_reviews['num_results'] == 0:
            author_none = open('no_review.txt', 'a')
            author_none.write(author)
            author_none.write("\n")
            author_none.close()
            df_reviews = pd.DataFrame()
        else:
            #Convert to dataframe
            df_reviews = pd.DataFrame(dict_reviews['results'])
            df_reviews = df_reviews[['book_author', "book_title", "byline", "publication_dt", "url"]]
    except:
        df_reviews = pd.DataFrame()
        print "DID NOT GET " + author
    #Append to rest of reviews
    full_reviews = full_reviews.append(df_reviews)

full_reviews.to_csv(csv_name, na_rep=np.nan, index=False, encoding="utf-8")
