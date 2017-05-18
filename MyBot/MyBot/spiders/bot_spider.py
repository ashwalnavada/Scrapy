import scrapy


class BotSpider(scrapy.Spider):
    name = "bot"
    allowed_domains = ['edx.org']
    start_urls = [
        'https://www.edx.org/course?course=all',
    ]

    def parse(self, response):
        for course in response.css('div.course'):
            yield {
                'title': course.css('span.title::text').extract_first()
            }