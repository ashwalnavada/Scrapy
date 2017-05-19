import scrapy
from scrapy.spiders import CrawlSpider, Rule, BaseSpider, Spider
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from courses.items import Course

class BotEdx(scrapy.Spider):
    name = 'edx'
    allowed_domain = ['edx.org']
    #start_urls = ['https://www.edx.org/course/ielts-academic-test-preparation-uqx-ieltsx-0#!']
    start_urls = ["https://www.edx.org/course?course=all"]
    #print start_urls

    rules = (
        Rule(LxmlLinkExtractor(
        	allow=('.*/course/.*', ),
        ), callback='parse_item'),

       Rule(LxmlLinkExtractor(
           allow=('.*/course/.*', ),
        )),
    )



    def parse_item(self, response):
        item = Course()
        item["institute"] = 'Edx'
        #item['title'] = response.xpath('//*[@id="course_intro_heading"]/text()').extract()
        #item['Length'] = response.xpath('//*[@id="block-list__desc"]/div/div/div[1]/div[1]/div[2]/div/p/span/text()').extract()[0]
        #item['credits'] = response.xpath('//*[@id="main"]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/p/text()').extract()[0][0]
        #item['description'] = response.xpath('//*[@id="main"]/div/div/div[1]/div[1]/div[3]/div/p/text()').extract()[0]
        yield item