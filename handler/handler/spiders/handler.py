# -*- coding: utf-8 -*-
import scrapy
from handler.items import HandlerItem

domain = 'usnpl.com'
start = 'http://usnpl.com'

class HouseSpider(scrapy.Spider):
    name = 'handler'
    allowed_domains = [domain]
    start_urls = [start]

    def parse(self, response):
        item = HandlerItem()
        item['link'] = []
        item['link2'] = []
        item['domainlink'] = []
        item['domainlink2'] = []
        item['twitterlink'] = []
        item['twitterlink2'] = []
        item['twitterlinku'] = []
        item['handles'] = []

        item['link'] = response.xpath('//a/@href').extract()

        item['twitterlink'] = [w for w in item['link'] if "twitter.com" in w]
        item['domainlink'] = [w for w in item['link'] if domain in w]
        for url in item['twitterlink']:
            item['twitterlinku'].append(url)
        for url in item['domainlink']:
            request = scrapy.Request(url, callback=self.parse2)
            request.meta['item'] = item
            yield request

        for link in item['twitterlinku']:
            handle = link.split(".com/")[1]
            if "/" in handle:
                handle = handle.split("/")[0]
            item['handles'].append(handle)
        yield item
        print (item['handles'])

    def parse2(self, response):
        item = response.meta['item']
        item['link2'] = response.xpath('//a/@href').extract()
        item['twitterlink2'] = [w for w in item['link2'] if "twitter.com" in w]
        for url in item['twitterlink2']:
            item['twitterlinku'].append(url)

        yield item
