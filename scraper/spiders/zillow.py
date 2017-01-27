from __future__ import absolute_import

import scrapy

from scraper.items import HomeListing

BASE_URL = 'http://zillow.com'


class ZillowScraper(scrapy.Spider):
    name = 'zillow'

    def start_requests(self):
        url = BASE_URL
        city = getattr(self, 'city', None)
        state = getattr(self, 'state', None)
        if city is not None and state is not None:
            url = url + '/' + city + '-' + state
        yield scrapy.Request(url, self.parse)

    def parse(self, response):

        # Grab all results on page
        homes = response.css('ul.photo-cards > li')
        for home in homes:
            listing = HomeListing()
            listing['link'] = BASE_URL + home.css('a.hdp-link::attr(href)').extract_first()
            article = home.css('article.zsg-photo-card.photo-card')
            listing['latitude'] = int(article.xpath('@data-latitude').extract_first())
            listing['longitude'] = int(article.xpath('@data-longitude').extract_first())
            listing['zid'] = int(article.xpath('@data-zpid').extract_first())
            listing['pgapt'] = article.xpath('@data-pgapt').extract_first()
            listing['sgapt'] = article.xpath('@data-sgapt').extract_first()
            address_info = article.css('.zsg-photo-card-content > span > span')
            for entry in address_info:
                type = entry.xpath('@itemprop').extract_first()
                if type == 'streetAddress':
                    listing['street_address'] = entry.xpath('text()').extract_first()
                elif type == 'addressLocality':
                    listing['city'] = entry.xpath('text()').extract_first()
                elif type == 'addressRegion':
                    listing['state'] = entry.xpath('text()').extract_first()
                elif type == 'postalCode':
                    listing['zip_code'] = int(entry.xpath('text()').extract_first())
            yield listing

