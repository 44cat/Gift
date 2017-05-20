# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GiftItem(scrapy.Item):
    # gift's name
    name = scrapy.Field()
    # gift's price
    price = scrapy.Field()
    # gift's picture
    picture = scrapy.Field()
    # how many people like this gift
    LikeNum = scrapy.Field()

