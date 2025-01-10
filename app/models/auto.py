from .journal import Journal
from ..extentions import db


class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.String(50))
    color = db.Column(db.String(50))
    mark = db.Column(db.String(50))
    personal_id = db.Column(db.Integer, db.ForeignKey('auto_personnel.id', ondelete='CASCADE'))
    records = db.relationship(Journal, backref='auto')
