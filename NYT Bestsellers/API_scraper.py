#No lists on paperback for 10/18/2008
import datetime
import json
import pycurl
import pandas as pd
import numpy as np
from StringIO import StringIO
from api import NYT_API

#Request JSON from API
def request_json(date_start, date_end):

    csv_name = str(date_start) + "_to_" + str(date_end) + ".csv"

    difference = date_end - date_start
    dates = [date_start + datetime.timedelta(days=x) for x in range(0, difference.days + 1, 7)]

    full_list = pd.DataFrame()

    for date in dates:

        if date >= datetime.date(2017, 02, 05):
            best_seller = ["trade-fiction-paperback", "hardcover-fiction", "combined-print-and-e-book-fiction"]
        elif date >= datetime.date(2011, 02, 13):
            best_seller = ["trade-fiction-paperback", "hardcover-fiction", "mass-market-paperback", "e-book-fiction"]
        else:
            best_seller = ["trade-fiction-paperback", "hardcover-fiction", "mass-market-paperback"]

        for bslist in best_seller:
            current_URL = "http://api.nytimes.com/svc/books/v2/lists/%s/%s.json?api-key=%s" %(date, bslist, NYT_API)
            buffer = StringIO()
            c = pycurl.Curl()
            c.setopt(c.URL, current_URL)
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            c.close()
            current_list = buffer.getvalue()
            try:
                dict_list = json.loads(current_list)
                if dict_list['status'] == "ERROR":
                    print "DID NOT GET" + str(date) + bslist
                    best_list = pd.DataFrame()
                else:
                    best_list = Make_DF(dict_list)
            except:
                best_list = pd.DataFrame()
                print "DID NOT GET" + str(date) + bslist
            #Append to rest of bestseller lists
            full_list = full_list.append(best_list)

    full_list.to_csv(csv_name, na_rep=np.nan, index=False, encoding="utf-8")

#Convert JSON to dataframe
def Make_DF(dict_list):
    df_list = pd.DataFrame(dict_list['results'])

    details_df = pd.DataFrame()
    for i in range(0, len(df_list)):
        details_df = details_df.append(pd.DataFrame(df_list['book_details'][i][0], index=[i]))

    reviews_df = pd.DataFrame()
    for i in range(0, len(df_list)):
        reviews_df = reviews_df.append(pd.DataFrame(df_list['reviews'][i][0], index=[i]))

    review_detail = pd.merge(details_df, reviews_df, how="inner", left_index=True, right_index=True)
    whole_list = pd.merge(df_list, review_detail, how="inner", left_index=True, right_index=True)
    best_list = whole_list[['display_name', 'published_date', 'rank', 'author', 'title', 'rank_last_week', 'weeks_on_list', 'book_review_link', 'sunday_review_link', 'age_group', 'price', 'publisher', 'description', 'contributor', 'contributor_note']]
    return best_list

#Request date endpoints
print "What date's best-seller list do you want to start with?  First, the year (YYYY):"
year_start = int(raw_input('> '))
print "Now the month (MM):"
month_start = int(raw_input('> '))
print "Now the day (DD):"
day_start = int(raw_input('> '))
print "What date's best-seller list do you want to end with? First, the year (YYYY):"
year_end = int(raw_input('> '))
print "Now the month (MM):"
month_end = int(raw_input('> '))
print "Now the day (DD):"
day_end = int(raw_input('> '))

date_start = datetime.date(year_start, month_start, day_start)
date_end = datetime.date(year_end, month_end, day_end)

request_json(date_start, date_end)
