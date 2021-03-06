from flask import render_template, jsonify
from flask import current_app
from app.photos import bp
from app.models import Photo
from app.bloba import get_img_url


@bp.route('/')
@bp.route('/index')
def index(img_url=None, names=None):
    img_albums = Photo.query.group_by(
        Photo.album).with_entities(Photo.album).all()
    img_url = []
    albums = []

    for i, album in enumerate(img_albums):
        container = str(img_albums[i])[2:-3]
        img_names = Photo.query.filter(
            Photo.album == container).with_entities(Photo.title).distinct()
        blob = str(img_names[i])[2:-3]

        img_url.append(get_img_url(blob, container))
        albums.append(container)

    return render_template('index.html', img_url=img_url, albums=albums, title='Home')


@bp.route('/about')
def about():
    img_albums = Photo.query.group_by(
        Photo.album).with_entities(Photo.album).all()
    img_url = []
    albums = []

    for i, album in enumerate(img_albums):
        container = str(img_albums[i])[2:-3]
        img_names = Photo.query.filter(
            Photo.album == container).with_entities(Photo.title).distinct()
        blob = str(img_names[i])[2:-3]

        img_url.append(get_img_url(blob, container))
        albums.append(container)

    return render_template('about.html', img_url=img_url, albums=albums, title='About')


@bp.route('/contact')
def contact():

    img_albums = Photo.query.group_by(
        Photo.album).with_entities(Photo.album).all()
    img_url = []
    albums = []

    for i, album in enumerate(img_albums):
        container = str(img_albums[i])[2:-3]
        img_names = Photo.query.filter(
            Photo.album == container).with_entities(Photo.title).distinct()
        blob = str(img_names[i])[2:-3]

        img_url.append(get_img_url(blob, container))
        albums.append(container)

    return render_template('contact.html', img_url=img_url, albums=albums, title='Contact')


@bp.route('/album/<album>')
def album(album):
    img_names = Photo.query.filter_by(
        album=album).with_entities(Photo.title).all()
    img_url = []
    albums = []

    for i in range(len(img_names)):
        blob = str(img_names[i])[2:-3]
        container = album
        img_url.append(get_img_url(blob, container))
        albums.append(container)

    return render_template('album.html', img_url=img_url, albums=albums, title=album)


@bp.route('/bg_proc')
def bg_proc():
    Photo.populate_db()
    return jsonify(gallery="updated!")
