# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


    # name = scrapy.Field()
class BzBlock(scrapy.Item):
    category = scrapy.Field() #store category (<h3>)
    origin = scrapy.Field() #store origin url 
    articles = scrapy.Field() # all article links on the url
    pass

class BzArtilce(scrapy.Item):
    url = scrapy.Field()
    author = scrapy.Field()
    categories = scrapy.Field()
    date = scrapy.Field()
    emotions = scrapy.Field()
    title = scrapy.Field()
    headline = scrapy.Field()
    text = scrapy.Field()
    pass
