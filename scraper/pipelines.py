from __future__ import absolute_import

import os

from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


class SqlAlchemyPipeline(object):
    def process_item(self, item, spider):
        print 'in pipeline'
        return item
