# -*- coding: utf-8 -*-
import scrapy

from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class Id97Spider(scrapy.Spider):
    name = 'id97'
    allowed_domains = ['id97.com']
    start_urls = ['http://www.id97.com/movie/?page=363']

    def parse(self, response):
        for sel in response.xpath("//div[@class='col-xs-12']/div[@class='col-xs-1-5 col-sm-4 col-xs-6 movie-item']"):

            # 详情页链接
            url = sel.xpath("div[@class='movie-item-in']/a/@href").extract_first()

            # 文章标题
            title = sel.xpath("div/a/@title").extract_first()



            # 测试 测试
            print(title)
            print(url)

        # 上一页链接
        next_pages = response.xpath("/html/body/div[1]/div[2]/ul/li[2]/a/@href").extract_first()

        

        print(next_pages)

        # if next_pages:
        #     # 对分页链接重新组合
        #     # next_page = urljoin(SITE_URL, next_pages[0].extract())
        #
        #     # 以 下一页链接为回调函数参数  重新执行爬取列表页数据
        #     yield scrapy.Request('http://www.id97.com'+next_pages, callback=self.parse, dont_filter=True)


    # 对单页详情页 进行数据爬取
    def parse_dir_contents(self, response):
        pass