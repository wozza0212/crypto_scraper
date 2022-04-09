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
        row = response.xpath("//tr[@class='cmc-table-row']")
        # This row, is the xpath to a row of the table that we want to access

        yield {
            'Date': row.path("./h1/text()").get(),
            'Name': row.xpath("./td/div/a[@class='cmc-table__column-name--name cmc-link']/text()").get(),
            'Symbol': row.xpath("./td/div/a[@class='cmc-table__column-name--symbol cmc-link']/text()").get(),
            'Price': row.xpath("./td[@class='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--rightcmc-table__cell--sort-by__price']/div/text()").get(),
            'Market Cap': row.xpath("./td[@class='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap']/text()").get(),
            'Circulating Supply': row.xpath("./td[@class='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply']/text()").get(),
            'url': response.url,

        }
