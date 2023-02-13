
from application import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.String(150))
    about = db.Column(db.String(10000))
    img = db.Column(db.String(150))
    users = db.relationship('User')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'))
