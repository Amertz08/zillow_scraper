from __future__ import absolute_import, unicode_literals, print_function

import re

from babel.numbers import parse_number
import scrapy

from scraper.items import HomeListing

BASE_URL = 'http://zillow.com'


class ZillowScraper(scrapy.Spider):
    name = 'zillow'

    def __init__(self, *args, **kwargs):
        super(ZillowScraper, self).__init__(*args, **kwargs)
        city = kwargs.get('city')
        state = kwargs.get('state')
        if not city:
            raise ValueError('city parameter not defined')
        if not state:
            raise ValueError('state parameter not defined')
        self.city = city
        self.state = state

    def start_requests(self):
        url = BASE_URL
        city = self.city
        state = self.state
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
            listing['list_price'] = 0.00  # TODO: actually scrape
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
                    listing['zip_code'] = entry.xpath('text()').extract_first()
            request = scrapy.Request(listing['link'], self.parse_detailed_view)
            request.meta['listing'] = listing
            yield request

            # next_page = response.css('li.zsg-pagination-next a::attr(href)').extract_first()
            # if next_page is not None:
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(next_page, callback=self.parse)

    def parse_detailed_view(self, response):
        listing = response.meta['listing']
        stats = response.css('span.addr_bbs::text')
        for stat in stats:
            text = stat.extract()
            ans = re.search('bed', text)
            if ans is not None:
                listing['beds'] = float(re.search('(\d\S*)', text).group())
            ans = re.search('bath', text)
            if ans is not None:
                listing['baths'] = float(re.search('(\d\S*)', text).group())
            ans = re.search('sqft', text)
            if ans is not None:
                val = re.search('(\d+\S+)', text).group()
                listing['sq_feet'] = parse_number(val, 'en_US')
        yield listing
