from .auto import Auto
from ..extentions import db


class Auto_personnel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    father_name = db.Column(db.String(50))
    autos = db.relationship(Auto, backref='person')
