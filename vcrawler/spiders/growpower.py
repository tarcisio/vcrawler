import html2text
import scrapy
from scrapy.spiders import SitemapSpider
from vcrawler.items import Product

converter = html2text.HTML2Text()

class GrowpowerSpider(SitemapSpider):
    name = "growpower"
    sitemap_urls = ['https://www.growpower.com.br/sitemap.xml']

    def _parse_description(self, response):
        description = ''
        rawdesc = response.css('div#descricao').extract_first()
        if rawdesc is not None:
            description = converter.handle(rawdesc)
        return description

    def _parse_category(self, response):
        category = ''
        categories = response.css('div.breadcrumbs a::text').extract()
        if len(categories) > 1:
            categories.pop(0)
            category = categories[0]
            category = category.strip()
        return category

    def parse(self, response):
        sku = response.css('span[itemprop="sku"]::text').extract_first()
        if sku is None:
            self.logger.info('A página não parece conter um produto. SKU não encontrado. %s', response.url)
            return

        name = response.css('h1.nome-produto::text').extract_first()
        price = response.xpath("//meta[@itemprop='price']").re(r'content="(.*?)"')[-1]

        product = Product()
        product['store'] = GrowpowerSpider.name
        product['sku'] = sku
        product['name'] = name
        product['price'] = price
        product['category'] = self._parse_category(response)
        product['url'] = response.url
        product['description'] = self._parse_description(response)
        return product