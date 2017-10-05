from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .app import db, login_manager

class Journey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(3000), unique=False, nullable=False)
    picture = db.Column(db.String(250), unique=False, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Reflection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(3000), unique=False, nullable=False)
    journeyid = db.Column(db.Integer, unique=False, nullable=False)
    journeyname = db.Column(db.Integer, unique=False, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    picture = db.Column(db.String(250), unique=False, nullable=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    journeyname = db.Column(db.Integer, unique=False, nullable=False)
    journeyid = db.Column(db.Integer, unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    q1 = db.Column(db.String(3000), unique=False, nullable=False)
    q2 = db.Column(db.String(3000), unique=False, nullable=False)
    q3 = db.Column(db.String(3000), unique=False, nullable=False)
    q4 = db.Column(db.String(3000), unique=False, nullable=False)
    q5 = db.Column(db.String(3000), unique=False, nullable=False)
    q6 = db.Column(db.String(3000), unique=False, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    group = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    user_type = db.Column(db.String(10), unique=False, nullable=False)
    
    def __init__(self, username, first_name, last_name, email,
                group, password, user_type):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.group = group
        self.password = password
        self.user_type = user_type

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
