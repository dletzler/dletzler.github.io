# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JeopardyItem(scrapy.Item):

    Season = scrapy.Field()
    Episode = scrapy.Field()
    Contestant1 = scrapy.Field()
    Contestant2 = scrapy.Field()
    Contestant3 = scrapy.Field()
    Round = scrapy.Field()
    Category = scrapy.Field()
    Value = scrapy.Field()
    Clue = scrapy.Field()
    Answer = scrapy.Field()
    Order = scrapy.Field()
    Right = scrapy.Field()
    Wrong1 = scrapy.Field()
    Wrong2 = scrapy.Field()
    DailyDouble = scrapy.Field()
    Wagered = scrapy.Field()
