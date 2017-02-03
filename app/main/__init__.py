from __future__ import absolute_import, print_function, unicode_literals

from flask import Blueprint, render_template

from app.models import HomeListing

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/listings')
def listings_view():
    lists = list(set(HomeListing.query.all()[::-1]))
    return render_template('listings.html', listings=lists)


@main.route('/listing/<int:zid>')
def listing_detailed(zid):
    listings = HomeListing.query.filter_by(zid=zid).all()[::-1]

    def price_gen(listings):
        for listing in listings:
            yield {
                'date': listing.entry_date,
                'price': listing.list_price
            }

    prices = [price for price in price_gen(listings)]
    return render_template('list_view.html', listing=listings[0], prices=prices)