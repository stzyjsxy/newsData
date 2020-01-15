# -*- coding: utf-8 -*-
import scrapy
from myspider.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    #allowed_domains = ['www.163.com/']
    start_urls = ['https://www.163.com//']

    def parse(self, response):
        # 体育栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/ul/li/a')
        # NBA/CBA栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/ul/li/a')
        # 中超/国际栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/ul/li/a')
        # 科技栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[10]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/ul[1]/li/a')
        # 手机栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[10]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/ul/li/a')
        # 娱乐栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[6]/div[1]/div/div/div[2]/div[1]/div[2]/div/ul[1]/li/a')
        # 影视娱乐栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[6]/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li/a')
        # 财经
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[8]/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/ul[1]/li/a')
        # 股票
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[8]/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/div/ul/li/a')
        # 商业
        node_list = response.xpath(
            '//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[8]/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/ul/li/a')

        items = []
        for node in node_list:
            item = NewsItem()
            url = node.xpath('./@href').extract()
            title = node.xpath('./text()').extract()
            item['url'] = url[0]
            item['title'] = title[0]
            items.append(item)
        return items
