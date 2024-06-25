import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = 'divannewpars'
    allowed_domains = ['market-sveta.ru']
    start_urls = ['https://www.market-sveta.ru/category/ljustry-podvesnye/']

    def parse(self, response):
        divans = response.css('div._sw-show-gall')
        for divan in divans:
            yield {
                'name': divan.css('div.name::text').get(),
                'prise': divan.css('div.prise ys_p::text').get(),
                'url': divan.css('a').attrib['href']
            }


