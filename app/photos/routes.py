from flask import render_template
from app.photos import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')
