from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from basic_crawler.items import BasicCrawlerItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request
import re


class MySpider(CrawlSpider):
	name = "basic_crawler"
	allowed_domains = ["udemy.com"]
	start_urls = ["https://www.udemy.com/courses/development/all-courses/",]

	rules = [Rule(LinkExtractor(allow=['/course/.*']), 'parse_story')]

	def parse_story(self, response):
		course = BasicCrawlerItem()
		#course['title'] = response.url
		course['title'] = response.xpath("//card__title/h1/text()").extract()
		#story['intro'] = response.css('p.introduction::text').extract()

		return course





	#name = "basic_crawler"
	#allowed_domains = ['edx.org']
	#start_urls = ["https://www.edx.org/course?course=all"]

	#def parse(self, response):
		#hxs = Selector(response)

		#print('Got a response from %s.' % response.url)
		#CODE for scraping book titles
		#titles = hxs.xpath('//span[@class="block-list__desc"]/text()').extract()
		#print('Title: %s \n' % titles)

	 	#for title in titles:
		#	course = BasicCrawlerItem()
		#	course["title"] = title
		#	yield course


		#visited_links=[]
		#links = hxs.xpath('//a/@href').extract()
        #       link_validator= re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")


		#
		#for link in links:
		#	if link_validator.match(link) and not link in visited_links:
		#		visited_links.append(link)
		#		yield Request(link, self.parse)
		#	else:
		#		full_url=response.urljoin(link)
		#		visited_links.append(full_url)
		#		yield Request(full_url, self.parse)
