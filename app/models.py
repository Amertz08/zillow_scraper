from __future__ import absolute_import, unicode_literals, print_function

import arrow
from datetime import date, datetime

from app import db


def filter_serialization(column):
    """Returns only values that can be turned into JSON"""
    if isinstance(column, datetime):
        return column.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(column, date):
        return column.strftime('%Y-%m-%d')
    elif column is None:
        return ''
    return column


def serial_gen(obj):
    """Generator to build serialized object"""
    if not isinstance(obj, db.Model):
        raise TypeError('Must be a Flask-SQLAlchemy object')
    for i in obj.__table__.columns:
        yield i.name, filter_serialization(getattr(obj, i.name))


class HomeListing(db.Model):
    __tablename__ = 'home_listings'

    id = db.Column(db.Integer, primary_key=True)
    zid = db.Column(db.Integer)
    entry_date = db.Column(db.Integer, default=arrow.now().timestamp)
    street_address = db.Column(db.String(255), default='', nullable=False)
    city = db.Column(db.String(255), default='', nullable=False)
    state = db.Column(db.String(2), default='', nullable=False)
    zip_code = db.Column(db.String(10), default='', nullable=False)
    list_price = db.Column(db.Float, default=0.00)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    pgapt = db.Column(db.String(25))
    sgapt = db.Column(db.String(25))
    link = db.Column(db.String(255))

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def serialize(self):
        """Returns all attributes in dict"""
        return {key: val for key, val in serial_gen(self)}


