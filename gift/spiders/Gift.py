# -*- coding: utf-8 -*-
import scrapy
from gift.items import GiftItem
import re

class GiftSpider(scrapy.Spider):
    name = "Gift"
    allowed_domains = ["liwushuo.com"]
    start_urls = ['http://www.liwushuo.com/posts/1048073']

    def parse(self, response):
        for l in response.xpath("//div[@class='content']"):
            item = GiftItem()
            item['name'] = l.xpath('h3/span[2]/text()').extract()
            item['picture'] = l.xpath("//img//@src").extract()
            item['price'] = l.xpath("//div/p[@class='item-info-price']/span/text()").extract()
            item['LikeNum'] = l.xpath("//div/p[@class='item-like-info']/text()").extract()
            yield item
