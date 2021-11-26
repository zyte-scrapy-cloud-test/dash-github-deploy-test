import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.org']
    start_urls = ['http://example.org/']

    def parse(self, response):
        pass
