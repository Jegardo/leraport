from flask import render_template
from flask import current_app
from app.photos import bp
from app.models import Photo


@bp.route('/')
@bp.route('/index')
def index(img_url=None, names=None):
    img_url = Photo.query.with_entities(Photo.img_url).first
    return render_template('index.html', names=names, img_url=img_url, title='Home')
