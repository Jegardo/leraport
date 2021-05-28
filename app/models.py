from app import db
from datetime import datetime, timedelta
from app.bloba import get_containers, get_img_names, get_img_url
from time import time


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    album = db.Column(db.String(64), index=True,)
    img_url = db.Column(db.String(420), index=True, unique=True)

    def __repr__(self):
        return '<Img {} from {}>'.format(self.title, self.album)

    def populate_db():
        containers = get_containers()

        for album in containers:
            blobs = get_img_names(album)
            for img in blobs:
                exists = db.session.query(Photo.id).filter_by(
                    title=img).first() is not None
                if exists:
                    continue

                url = get_img_url(img, album)
                p = Photo(title=img, album=album, img_url=url[0])
                db.session.add(p)
                db.session.commit()
