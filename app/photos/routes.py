from flask import render_template
from flask import current_app
from app.photos import bp
from app.models import Photo
from app.bloba import get_img_url


@bp.route('/')
@bp.route('/#')
def index(img_url=None, names=None):
    img_names = Photo.query.group_by(
        Photo.album).with_entities(Photo.title).all()
    img_albums = Photo.query.group_by(
        Photo.album).with_entities(Photo.album).all()
    img_url = []

    for i in range(len(img_albums)):
        blob = str(img_names[i])[2:-3]
        container = str(img_albums[i])[2:-3]
        img_url.append(get_img_url(blob, container))

    return render_template('base.html', img_url=img_url, title='Home')


@bp.route('/#About')
def about():
    return render_template('about.html', title='About')
