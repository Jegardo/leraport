from flask import render_template
from flask import current_app
from app.photos import bp
from app.bloba import get_img_url, get_img_names


@bp.route('/')
@bp.route('/index')
def index(img_url=None, names=None):
    img_url = get_img_url('Skapolit,_Benono,_Madagaskar.jpg', 'pic')
    names = get_img_names('pic2')
    return render_template('index.html', names=names, img_url=img_url, title='Home')
