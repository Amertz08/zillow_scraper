from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import config

db = SQLAlchemy()


def create_app(config_lvl):
    app = Flask(__name__)
    app.config.from_object(config[config_lvl])
    Bootstrap(app)
    db.init_app(app)

    # Blueprints

    return app