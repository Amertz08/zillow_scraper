from __future__ import absolute_import

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or '(7z)=cz$)mu#ys(+2rra$uhh1h^uboaviz4&!vh!^yf=(@6p)x'

    MYSQL_USER = 'zillow'
    MYSQL_PASS = '7R1SzZpHWhzl'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'zillow_scraper'
    # Database info
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{usr}:{passwd}@{host}/{db}'.format(
        usr=MYSQL_USER, passwd=MYSQL_PASS, host=MYSQL_HOST, db=MYSQL_DB
    )

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    PRODUCTION = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}