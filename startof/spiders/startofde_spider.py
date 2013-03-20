from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from startof.items import StartofItem
import HTMLParser

class StartofdeSpider(CrawlSpider):
    name = "startofde"
    allowed_domains = ["www.start-of.de", "start-of.de"]
    start_urls = [
        "http://start-of.de/"
    ]
    rules = [Rule(SgmlLinkExtractor(allow=[r'profiles/\w+']), callback='parse_profile')]
    handle_httpstatus_list = [404]

    def parse_profile(self, response):
        hxs = HtmlXPathSelector(response)
        h = HTMLParser.HTMLParser()
        item = StartofItem()
        
        u = lambda s: h.unescape(s).encode("utf-8")
        
        item['name'] = u(hxs.select('//*[@itemprop="name"]/text()').extract()[0])
        item['email'] = u(hxs.select('//*[@itemprop="email"]/text()').extract()[0])
        item['url'] = u(hxs.select('//*[@itemprop="url"]/text()').extract()[0])
        return item
