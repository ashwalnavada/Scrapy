from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
 
class ExampleSpider(CrawlSpider):
    name = "ant" #Spider name
    allowed_domains = ["codecademy.com"] # Which (sub-)domains shall be scraped?
    start_urls = ["https://www.codecademy.com/learn"] # Start with this one
 
    # Follow any link scrapy finds (that is allowed and matches the patterns).
    rules = [Rule(LinkExtractor(allow=(r'/learn/.+'), deny=()), callback='parse_item', follow=True)] 
 
    def parse_item(self, response):
 
        print('Got a response from %s.' % response.url)
 
        selector = Selector(response)
 
        title_selector_str = '/html/body/div[2]/section/section/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/text()'
        #posttext_selector_str = '//article/div[@class="post-content"]//text()'
 
        title = selector.xpath(title_selector_str).extract()
        #post = selector.xpath(posttext_selector_str).extract()
 
        print('Title: %s \n' % title)
        #print('Content: %s \n' % post)
        
    