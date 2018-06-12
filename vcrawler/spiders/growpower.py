import html2text
import scrapy
from scrapy.spiders import SitemapSpider
from vcrawler.items import Product

converter = html2text.HTML2Text()

class GrowpowerSpider(SitemapSpider):
    name = "growpower"

    sitemap_urls = ['https://www.growpower.com.br/sitemap.xml']

    def parse(self, response):
        sku = response.css('span[itemprop="sku"]::text').extract_first()
        name = response.css('h1.nome-produto::text').extract_first()
        
        description = response.css('div#descricao').extract_first()
        description = converter.handle(description)

        price = response.xpath("//meta[@itemprop='price']").re(r'content="(.*?)"')[-1]

        product = Product()
        product['store'] = GrowpowerSpider.name
        product['sku'] = sku
        product['url'] = response.url
        product['name'] = name
        product['price'] = price
        product['description'] = description
        return product