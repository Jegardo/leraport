from app import db
from datetime import datetime, timedelta
from azure.storage.blob import generate_container_sas, ContainerSasPermissions
from time import time


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    album = db.Column(db.String(64), index=True, unique=True)
    img_url = db.Column(db.String(420), index=True, unique=True)

    def __repr__(self):
        return '<Post {}>'.format(self.body)
