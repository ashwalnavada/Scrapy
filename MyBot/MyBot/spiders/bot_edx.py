import scrapy

class BotEdx(scrapy.Spider):
    name = 'edx'
    allowed_domains = ['edx.org']
    start_urls = ['https://www.edx.org/course?course=all']

    def parse_item(self, response):
        item = Course()
        item["institute"] = 'Edx'
        item['title'] = response.xpath('//*[@id="main"]/div/div/div[1]/div[1]/div[1]/h1/text()').extract()[0]
        item['id'] = response.xpath('//*[@id="main"]/div/div/div[1]/div[1]/div[2]/div/p/span/text()').extract()[0]
        item['credits'] = response.xpath('//*[@id="main"]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/p/text()').extract()[0][0]
        item['description'] = response.xpath('//*[@id="main"]/div/div/div[1]/div[1]/div[3]/div/p/text()').extract()[0]
        yield item