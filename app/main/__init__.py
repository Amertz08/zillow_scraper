from __future__ import absolute_import, print_function, unicode_literals

from flask import Blueprint, render_template

from app.models import HomeListing

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/listings')
def listings():
    listings = HomeListing.query.all()
    return render_template('listings.html')
