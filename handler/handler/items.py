# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HandlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    link2 = scrapy.Field()
    domainlink = scrapy.Field()
    domainlink2 = scrapy.Field()
    twitterlink = scrapy.Field()
    twitterlink2 = scrapy.Field()
    twitterlinku = scrapy.Field()
    handles = scrapy.Field()
    pass
