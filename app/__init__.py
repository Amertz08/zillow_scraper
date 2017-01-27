from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from config import config

db = SQLAlchemy()
migrate = Migrate(app=None, db=db)


def create_app(config_lvl):
    app = Flask(__name__)
    app.config.from_object(config[config_lvl])
    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app)

    # Blueprints
    from main import main
    app.register_blueprint(main)

    return app