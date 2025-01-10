from ..extentions import db
from datetime import datetime


class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_out = db.Column(db.String(50))
    time_in = db.Column(db.String(50))
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id', ondelete='CASCADE'))
    auto_id = db.Column(db.Integer, db.ForeignKey('auto.id', ondelete='CASCADE'))
