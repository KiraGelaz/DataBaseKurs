from .journal import Journal
from ..extentions import db


class Routes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    records = db.relationship(Journal, backref='route')
