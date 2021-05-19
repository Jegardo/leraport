from flask import Flask, current_app
from flask_bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from app.photos import bp as photos_bp
    app.register_blueprint(photos_bp)

    return app
