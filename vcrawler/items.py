# -*- coding: utf-8 -*-

import scrapy

class Product(scrapy.Item):
    store        = scrapy.Field()
    sku          = scrapy.Field()
    url          = scrapy.Field()
    name         = scrapy.Field()
    price        = scrapy.Field()
    description  = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)