#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals, print_function
import os
import sys

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
import pytest

from app import create_app, db
from app.models import HomeListing
from app.tasks import crawl_

application = create_app(os.getenv('APP_CONFIG') or 'default')


def make_shell_context():
    return dict(
        app=application, db=db, HomeListing=HomeListing
    )

manager = Manager(application)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))


def input(message):
    """Remove if building w/ Py3"""
    return raw_input(message)


@manager.command
def createdb():
    """Setups db initially"""
    ans = input('Initialize DB? [y/n]: ').lower()
    if ans == 'y':
        db.create_all()
        print('DB initialized...')


@manager.command
def resetdb():
    """Resets db"""
    ans = input('Reset db? [y/n]: ').lower()
    if ans == 'y':
        db.drop_all()
        db.create_all()
        print('DB reset...')


@manager.command
def test():
    """Runs tests :)"""
    pytest.main()  # TODO: doesn't work


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
    print('Crawling: {0}, {1}'.format(city, state))
    crawl_(city, state)  # TODO: does not work. Also should be crawl_.delay(city, state) when it does.


if __name__ == '__main__':
    manager.run()
