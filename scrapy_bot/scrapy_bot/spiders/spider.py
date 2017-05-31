from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
 
class ExampleSpider(CrawlSpider):
    name = "ant" #Spider name
    allowed_domains = ["edx.org"] # Which (sub-)domains shall be scraped?
    start_urls = ["https://www.edx.org/course?course=all"] # Start with this one
 
    # Follow any link scrapy finds (that is allowed and matches the patterns).
    #rules = [Rule(LinkExtractor(allow=(r'/course/.+'), deny=()), callback='parse_item', follow=True)] 
 

    rules = [

        Rule(LinkExtractor(
            allow=('.*/course/.*', ),
        ),  callback='parse_item')
    ]
    def parse_item(self, response):
 
        #print('Got a response from %s.' % response.url)
 
        hx = Selector(response)
 
        #print('Got hx %s.' % hx)
        #title_selector_str = '//*[@id="course-intro-heading"]/text()'
        #posttext_selector_str = '//article/div[@class="post-content"]//text()'
 
        title = hx.xpath('//*[@id="course-info-page"]/header/div/div/div[2]/p/text()').extract()
        #post = selector.xpath(posttext_selector_str).extract()
 
        print('Title: %s \n' % title)
        #print('Content: %s \n' % post)

