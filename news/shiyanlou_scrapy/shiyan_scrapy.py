import scrapy

class Shiyanlou_warehouse(scrapy.Spider):

    name = 'Shiyanlou-github-warehouse'

    @property
    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for course in response.css('#user-repositories-list'):
            yield{
                'name': course.css('div.d-inline-block.mb-1 > h3 > a::text').extract_first().strip(),
                'update_time': course.css('div.f6.text-gray.mt-2 > relative-time::attr(datetime)').extract_first()
            }

# css
#user-repositories-list > ul > li:nth-child(1) > div.d-inline-block.mb-1 > h3 > a
#user-repositories-list > ul > li:nth-child(1) > div.f6.text-gray.mt-2 > relative-time


# xpath

# name = [i.strip() for i in response.xpath('//div[@class="d-inline-block mb-1"]/h3/a/text()').extract()]

#name = [i.strip() for i in response.css('div.d-inline-block.mb-1 > h3 > a::text').extract()]
#updatetime = [i.strip() for i in response.css('div.f6.text-gray.mt-2 > relative-time::attr(datetime)').extract()]


# if __name__ == "__main__":
#     u = Shiyanlou_warehouse()
#     print(u.start_requests())
