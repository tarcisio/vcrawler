# -*- coding: utf-8 -*-

import scrapy

class Product(scrapy.Item):
    store        = scrapy.Field()
    sku          = scrapy.Field()
    name         = scrapy.Field()
    price        = scrapy.Field()
    category     = scrapy.Field()
    url          = scrapy.Field()
    description  = scrapy.Field()