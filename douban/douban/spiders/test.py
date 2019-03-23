# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http.response.html import HtmlResponse


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com']
    # allowed_domains = ['www.bilibili.com']
    # start_urls = ['http://www.bilibili.com']

    def parse(self, response):
        res = response.xpath('//div[@id="anony-nav"]')
        a_list = res.xpath('.//a[@target="_blank"]/@href').extract()[0:3]
        print(a_list)
        book_url = a_list[0]
        print('book_url is begin')
        yield Request(url = book_url, callback=self.book_parse, dont_filter = True)
        print('book_url is finish')

        movie_url = a_list[1]
        print('movie_url is begin')
        print(movie_url)
        yield Request(url=movie_url, callback=self.movie_parse, dont_filter=True)
        print('movie_url is finish')

        music_url = a_list[2]
        print('music_url is begin')
        yield Request(url=music_url, callback=self.music_parse, dont_filter=True)
        print('music_url is finish')


    def book_parse(self, response):
        print(123)
        #print(response.body)
        res = response.xpath('//ul[@class="hot-tags-col5 s"]')
        # print('the res is ', res)
        a_list = res.xpath('.//a[@class="tag"]/@href').extract()
        for i in a_list:
            url = 'https://book.douban.com/' + i
            print('url is ', url)

        print('book is ok')

    def movie_parse(self, response):
        print('movie is ok')

    def music_parse(self, response):
        #电影信息都向这个URL请求
        movie_info_url = 'https://movie.douban.com/j/search_subjects?type= %s& tag= %s &sort=recommend&page_limit= %s &page_start= %s'
        Tv_Tag = ['热门', '国产剧', '综艺', '美剧', '日剧', '韩剧', '日本动画', '纪录片']
        Movie_Tag = ['热门', '最新', '豆瓣高分', '冷门佳片', '华语', '欧美', '韩国', '日本']
        Type = {'tv': Tv_Tag, 'movie': Movie_Tag}



        print('music is ok')
