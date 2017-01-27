from __future__ import absolute_import, print_function, unicode_literals

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from app import celery
from scraper.spiders.zillow import ZillowScraper


@celery.task
def crawl_(city, state):
    spider = ZillowScraper(city=city, state=state)
    crawl_process = CrawlerProcess(get_project_settings())
    crawl_process.crawl(spider)
    crawl_process.start()  # TODO: this doesn't work
