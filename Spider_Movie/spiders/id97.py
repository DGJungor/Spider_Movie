# -*- coding: utf-8 -*-
import scrapy


class Id97Spider(scrapy.Spider):
    name = 'id97'
    allowed_domains = ['id97.com']
    start_urls = ['http://www.id97.com/movie']

    def parse(self, response):
        for sel in response.xpath("//div[@class='col-xs-12']/div[@class='col-xs-1-5 col-sm-4 col-xs-6 movie-item']"):

            # 文章标题
            title = sel.xpath("div/a/@title").extract()

            # 测试 测试
            print(title[0])
