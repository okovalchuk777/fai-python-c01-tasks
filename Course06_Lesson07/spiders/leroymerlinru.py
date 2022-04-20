import scrapy
from scrapy.http import HtmlResponse
from lmparser.items import LmparserItem
from scrapy.loader import ItemLoader


class LeroymerlinruSpider(scrapy.Spider):
    name = 'leroymerlinru'
    allowed_domains = ['castorama.ru']
    start_urls = ['https://www.castorama.ru/gardening-and-outdoor/outdoor-furniture/tables-chairs-armchairs-and-benches/']

    # def __init__(self, name=None, **kwargs):
    #     super().__init__(name, **kwargs)
    #     self.start_urls = [f"https://www.avito.ru/rossiya?q={kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        # response.status
        next_page = response.xpath("//a[contains(@class,'next i-next')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[contains(@class,'product-card__name')]/@href")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):

        loader = ItemLoader(item=LmparserItem(), response=response)
        loader.add_xpath('name', "//h1[contains(@itemprop,'name')]/text()")
        loader.add_xpath('price', "//span[@class='price']//span/text()")
        loader.add_xpath('photos', "//div[@class='js-zoom-container']/img[contains(@class,'top-slide_')]/@data-src")
        loader.add_value('url', response.url)
        yield loader.load_item()

        # name = response.xpath("//h1[contains(@itemprop,'name')]/text()").get()
        # price = response.xpath("//span[@class='price']//span/text()").get()
        # # Scrapy return Base64 of Image Url after 10 images
        # # https://stackoverflow.com/questions/52676872/scrapy-return-base64-of-image-url-after-10-images
        # # So simple then get Data-src of Image instead of src.
        # # src - не работает корректно и выдаёт (data:image/png) и нужно использовать просто data-src
        # photos = response.xpath("//div[@class='js-zoom-container']/img[contains(@class,'top-slide_')]/@data-src").getall()
        # url = response.url
        # yield LmparserItem(name=name, price=price, photos=photos, url=url)
