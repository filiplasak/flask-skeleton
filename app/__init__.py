from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

app.config.from_object(config)

db = SQLAlchemy(app)

import models

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

import views
