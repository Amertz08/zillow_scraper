from __future__ import absolute_import, unicode_literals, print_function

from app import db


class HomeListing(db.Model):
    __tablename__ = 'home_listings'

    id = db.Column(db.Integer, primary_key=True)
    zid = db.Column(db.Integer)
    entry_date = db.Column(db.Integer, server_default=db.func.now())
    street_address = db.Column(db.String(255), default='', nullable=False)
    city = db.Column(db.String(255), default='', nullable=False)
    state = db.Column(db.String(255), default='', nullable=False)
    zip_code = db.Column(db.String(10), default='', nullable=False)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    pgapt = db.Column(db.String(25))
    sgapt = db.Column(db.String(25))
    link = db.Column(db.String(255))

