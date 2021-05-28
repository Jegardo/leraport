from app import db
from datetime import datetime, timedelta
from app.bloba import get_containers, get_img_names, get_img_url
from time import time


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    album = db.Column(db.String(64), index=True, unique=True)
    img_url = db.Column(db.String(420), index=True, unique=True)

    def __repr__(self):
        return '<Post {}>'.format(self.body)
