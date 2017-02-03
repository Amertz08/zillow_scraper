from __future__ import absolute_import, unicode_literals, print_function

import scrapy


class HomeListing(scrapy.Item):
    zid = scrapy.Field()
    street_address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip_code = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    pgapt = scrapy.Field()  # TODO: what does this mean?
    sgapt = scrapy.Field()  # TODO: what does this mean?
    link = scrapy.Field()
    list_price = scrapy.Field()
