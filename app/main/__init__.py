from __future__ import absolute_import, print_function, unicode_literals

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    pass