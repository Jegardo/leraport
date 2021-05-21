from flask import render_template
from app.photos import bp
from app.bloba import get_img_url


@bp.route('/')
@bp.route('/index')
def index(img_url=None):
    img_url = get_img_url('Skapolit,_Benono,_Madagaskar.jpg', 'pic')
    return render_template('index.html', img_url=img_url, title='Home')
