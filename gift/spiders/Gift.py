# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
# from scrapy.spider import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
from gift.items import GiftItem

class GiftSpider(scrapy.Spider):
    name = "Gift"
    allowed_domains = ["liwushuo.com"]
    start_urls = ["http://www.liwushuo.com/posts/1048001"]
    # base_url = "http://www.liwushuo.com/posts/"
    # rules = (
    #     Rule(LinkExtractor(allow='http://www.liwushuo.com/posts/\d{1,7}'),callback='parse',follow=True),
    # )

    # def start_requests(self):
    #     for i in range(1048001,1048003):
    #         url = self.base_url + str(i)
    #         yield Request(url,self.parse)

    def parse(self, response):
        for l in response.xpath("//div[@class='content']"):
            item = GiftItem()
            item['name'] = l.xpath('h3/span[2]/text()').extract()
            item["picture"] = l.xpath("//img//@src").extract()
            pic_list = item['picture']
            item["picture"] = [pic[:-5] for pic in pic_list][:-1]
            # pic_lst = []
            # for i in pic_list:
            #     pic = pic_lst.append(i)
            #     item["picture"] = pic[:-5]
            # item['picture'] = str(l.xpath("//img//@src").extract()).replace('-w720', '')
            item['price'] = l.xpath("//div/p[@class='item-info-price']/span/text()").extract()
            item['LikeNum'] = l.xpath("//div/p[@class='item-like-info']/text()").extract()
            yield item

