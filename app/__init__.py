from flask import Flask, current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from azure.storage.blob import BlobServiceClient
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    app.blob_service = BlobServiceClient(account_url="https://{}.blob.core.windows.net/".format([app.config['AZURE_NAME']]),
                                         account_key=[app.config['AZURE_STORAGE_KEY']])

    from app.photos import bp as photos_bp
    app.register_blueprint(photos_bp)

    return app


from app import models
