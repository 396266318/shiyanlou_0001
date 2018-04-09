# -*- coding:utf-8 -*-
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    """ 所有scrapy 爬虫需要写一个Spider类 这个类要继承scrapy.Spider 类, 在这个类中定义请求的网站和链接，如何从返回的网页提取数据等等 """

    name = 'shiyanlou-sourses'

    def start_requests(self):
        """ 需要返回一个可迭代的对象。迭代的元素是 'scrapy.Request' 对象，可迭代对象是一个列表或者迭代器，这样 scrapy 就知道有哪些网站需要爬取了。'scrapy.Request'接受第一个url 参数和一个callback 参数,url 指明要爬取的网页, callback 是一个回调函数用于处理返回的网页,通常是一个提起数据的 parse 函数. """
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        urls = (url_tmpl.format(i) for i in range(1, 23))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ 这个方法作为 'scrapy.Request'的 callback, 在里面编写提取数据的代码, scrapy 中的下载器会下载‘start_requests’ 中定义的每个 ‘Request’ 并且结果封装为一个 respone d对象传入这个方法 """
        for course in response.css('div.course-body'):
            yield {
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'tepy': course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d*]')
            }
