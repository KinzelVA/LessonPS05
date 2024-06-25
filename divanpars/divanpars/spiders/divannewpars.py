import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css("div._c9h0M")
        for divan in divans:
            yield {
                "name": divan.css("div.lsooF::text").get(),
                "prise": divan.css("div.pY3d2 span::text").get(),
                "url": divan.css("a").attrib["href"]
            }


