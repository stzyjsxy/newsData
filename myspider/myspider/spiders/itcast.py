#!urs/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from myspider.items import itcastItem
# 如果itcastItem是红色,可将左侧的myspider设置为根目录,右键markdirectory as sources root

# 以下三行是在 Python2.x版本中解决乱码问题，Python3.x 版本的可以去掉
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # allowed_domains = ['itcast.cn']
    # start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)
    # 网易新闻
    #start_urls = ("https://www.163.com",)
    start_urls = ("https://www.163.com","https://news.163.com/domestic/",)
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
        #node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[1]/div[2]/div[10]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div//a')

        # 娱乐栏
        node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/div[1]/div[2]/div//a')
        # 影视娱乐栏
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[6]/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li/a')
        # 财经
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[8]/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/ul[1]/li/a')
        # 股票
        # node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[8]/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/div/ul/li/a')
        # 商业
        #node_list = response.xpath('//*[@id="js_index2017_wrap"]/div[1]/div[2]/div[10]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/ul/li/a')

        # 热点新闻
        #node_list = response.xpath('//*/div/div[3]/div[4]/div[1]/div/div/ul/li/div//h3/a')


        items = []
        for node in node_list:
            item = itcastItem()
            url = node.xpath('./@href').extract()
            title = node.xpath('./text()').extract()
            item['url'] = url[0]
            item['title'] = title[0]
            items.append(item)
        return items

        # a = response.body
        # with open("itcast.text","w")as f:
        #     f.write(a)


