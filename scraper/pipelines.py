from __future__ import absolute_import, unicode_literals, print_function

import os

from scrapy.exceptions import DropItem
from sqlalchemy import exc as sqlalchemy_exc

from app import create_app, db
from app.models import HomeListing
from app.lib import commit

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


class SqlAlchemyPipeline(object):

    def __init__(self):
        self.zid_seen = set()

    def process_item(self, item, spider):
        if item['zid'] in self.zid_seen:
            raise DropItem('Duplicate listing found %s' % item['zid'])
        else:
            self.zid_seen.add(item['zid'])
            home = HomeListing(**item)
            with app.app_context():
                db.session.add(home)
                try:
                    commit(db.session)
                    return item
                except sqlalchemy_exc.SQLAlchemyError as e:
                    print(e)  # TODO logging
