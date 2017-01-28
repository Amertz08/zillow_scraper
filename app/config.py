from __future__ import absolute_import, unicode_literals, print_function

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or '(7z)=cz$)mu#ys(+2rra$uhh1h^uboaviz4&!vh!^yf=(@6p)x'

    MYSQL_USER = 'zillow'
    MYSQL_PASS = '7R1SzZpHWhzl'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'zillow_dev'
    # Database info
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{usr}:{passwd}@{host}/{db}'.format(
        usr=MYSQL_USER, passwd=MYSQL_PASS, host=MYSQL_HOST, db=MYSQL_DB
    )

    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULTS_BACKED = 'redis://localhost:6379/0'

    # flask_mail
    MAIL_SERVER = ''
    MAIL_PORT = 25

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

    MYSQL_USER = 'zillow'
    MYSQL_PASS = '7R1SzZpHWhzl'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'zillow_test'
    # Database info
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{usr}:{passwd}@{host}/{db}'.format(
        usr=MYSQL_USER, passwd=MYSQL_PASS, host=MYSQL_HOST, db=MYSQL_DB
    )


class ProductionConfig(Config):
    PRODUCTION = True

    MYSQL_USER = 'zillow'
    MYSQL_PASS = os.getenv('MYSQL_PASS') or '7R1SzZpHWhzl'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'zillow'
    # Database info
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{usr}:{passwd}@{host}/{db}'.format(
        usr=MYSQL_USER, passwd=MYSQL_PASS, host=MYSQL_HOST, db=MYSQL_DB
    )

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
