from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cachebuster import CacheBuster

app = Flask(__name__)
app.config['SECRET_KEY'] = '9876543210-this-is-my-key-not-yours-0123456789'
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Create cache buster
cache_buster = CacheBuster(config={'extensions': ['.js', '.css', '.json'], 'hash_size': 5})
cache_buster.init_app(app)

from app import routes, models
