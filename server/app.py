# server/app.py

from flask import Flask, request, session
from flask_restful import Resource
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from config import db, api  
from models import User, Blog, Tag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "shhh-very-secret"


db.init_app(app)
api.init_app(app)
migrate = Migrate(app, db)


