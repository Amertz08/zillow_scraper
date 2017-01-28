from __future__ import absolute_import, print_function, unicode_literals

import arrow
from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from app.config import config, Config

db = SQLAlchemy()
migrate = Migrate(app=None, db=db)
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
mail = Mail()


def create_app(config_lvl):
    app = Flask(__name__)
    app.config.from_object(config[config_lvl])
    Bootstrap(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    celery.conf.update(app.config)

    # Filters and Context processors
    @app.template_filter('datetime')
    def datetime(date):
        return arrow.get(date).format('YYYY-MM-DD hh:mm:ss')

    # Blueprints
    from app.main import main
    app.register_blueprint(main)
    return app