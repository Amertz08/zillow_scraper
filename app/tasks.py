from __future__ import absolute_import, print_function, unicode_literals

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from app import celery, mail
from scraper.spiders.zillow import ZillowScraper


@celery.task
def crawl_(city, state):
    print('In task: {0}, {1}'.format(city, state))
    spider = ZillowScraper(city=city, state=state)
    crawl_process = CrawlerProcess(get_project_settings())
    crawl_process.crawl(spider)
    crawl_process.start()  # TODO: this doesn't work
    # http://stackoverflow.com/questions/11528739/running-scrapy-spiders-in-a-celery-task


@celery.task
def send_async_email(msg):
    mail.send(msg)
