from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index = True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    comments = db.relationship('comment', backref='post', lazy=True)

    def __repr__(self):
        return f"Pitch ( '{self.title}')"