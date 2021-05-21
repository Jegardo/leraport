import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alexopoulou-lera'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AZURE_NAME = os.environ.get('AZURE_NAME')
    AZURE_STORAGE_KEY = os.environ.get('AZURE_STORAGE_KEY')
    AZURE_STORAGE_CONNECTION_STRING = os.environ.get(
        'AZURE_STORAGE_CONNECTION_STRING')
