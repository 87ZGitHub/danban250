# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    #pic = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    rating = scrapy.Field()
    critical = scrapy.Field()
    quote = scrapy.Field()
