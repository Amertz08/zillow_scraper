from __future__ import absolute_import, print_function, unicode_literals

import arrow
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from app.config import config

db = SQLAlchemy()
migrate = Migrate(app=None, db=db)


def create_app(config_lvl):
    app = Flask(__name__)
    app.config.from_object(config[config_lvl])
    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app)

    # Filters and Context processors
    @app.template_filter('datetime')
    def datetime(date):
        return arrow.get(date).format('YYYY-MM-DD hh:mm:ss')

    # Blueprints
    from app.main import main
    app.register_blueprint(main)

    return app