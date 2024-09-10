from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=True)