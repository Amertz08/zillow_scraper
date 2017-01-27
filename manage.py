#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals, print_function
import os
import sys

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from app import create_app, db
from app.models import HomeListing
from scraper.spiders.zillow import ZillowScraper

application = create_app(os.getenv('APP_CONFIG') or 'default')
crawl_process = CrawlerProcess(get_project_settings())

def make_shell_context():
    return dict(
        app=application, db=db, HomeListing=HomeListing
    )

manager = Manager(application)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def createdb():
    db.create_all()


@manager.option('-c', '--city', help='City name', default=None)
@manager.option('-s', '--state', help='States short name', default=None)
def crawl(city, state):
    if city is None and state is None:
        print('A City name and State short name must be entered.')
        sys.exit()
    if len(state) > 2:
        print('You did not enter a proper length state abbreviation')
        sys.exit()
    city = city.lower()
    state = state.lower()
    print('Crawl: {0}, {1}'.format(city, state))
    spider = ZillowScraper(city=city, state=state)
    crawl_process.crawl(spider)
    crawl_process.start()


if __name__ == '__main__':
    manager.run()
