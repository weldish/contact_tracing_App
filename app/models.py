
from app import db
from datetime import datetime

class Todo(db.Model):             # a todolist class for my table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    described = db.Column(db.Text, nullable=False)
    content_added_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    complete=db.Column(db.Boolean)

class User(db.Model):             # a users class of infected and not infected popele
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique= True, nullable=False)
    infected= db.Column(db.Boolean)
    beacon_key=db.Column(db.String(100), unique= True, nullable=False)


class Exposures(db.Model):             # a users class of infected and not infected popele
    id = db.Column(db.Integer, primary_key=True)
    contactPersonA = db.Column(db.String(100), unique= True, nullable=False)
    contactPersonB = db.Column(db.String(100), unique= True, nullable=False)
    DateOfContact= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id') ,nullable=False)
