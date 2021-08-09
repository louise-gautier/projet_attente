import os

from pywebpush import webpush

from lib.tools import read_config, get_db_uri

basedir = os.path.abspath(os.path.dirname(__file__))

credentials = read_config('config_credentials.yaml')['db']


class Config(object):
    # FORMS
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9876543210-this-is-my-key-not-yours-0123456789'

    # DATABASE
    SQLALCHEMY_DATABASE_URI = get_db_uri(**credentials)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
