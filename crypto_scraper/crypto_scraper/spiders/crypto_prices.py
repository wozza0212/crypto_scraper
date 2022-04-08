import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CryptoPricesSpider(CrawlSpider):
    name = 'crypto_prices'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/historical']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="historical-link cmc-link"]'), callback='parse_item', follow=True),
    )
        # Set restrict_xpaths to the xpath or the links you want to follow

    def parse_item(self, response):
        print(response.url)
