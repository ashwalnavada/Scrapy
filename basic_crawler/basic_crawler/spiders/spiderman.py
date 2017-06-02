from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from basic_crawler.items import BasicCrawlerItem
from scrapy.http import Request
import re


class MySpider(BaseSpider):
	name = "basic__crawler"
	allowed_domains = ['codecademy.com']
	start_urls = ["https://www.codecademy.com/learn"]

	def parse(self, response):
		hxs = Selector(response)

		#CODE for scraping titles from website
		titles = hxs.xpath('/html/body/div[2]/section/section/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/text()').extract()
	 	for title in titles:
			course = BasicCrawlerItem()
			course["title"] = title
			yield course

		
		#CODE for scraping description
		description = hxs.xpath('/html/body/div[2]/section/section/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div/p/text()').extract()
		for desc in description:
			course_2 = BasicCrawlerItem()
			course_2["desc"] = desc
			yield course_2
		

		visited_links=[]
		links = hxs.xpath('//a/@href').extract()
                link_validator= re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

		for link in links:
			if link_validator.match(link) and not link in visited_links:
				visited_links.append(link)
				yield Request(link, self.parse)
			else:
				full_url=response.urljoin(link)
				visited_links.append(full_url)
				yield Request(full_url, self.parse)