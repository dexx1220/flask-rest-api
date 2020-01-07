from datetime import datetime
from config import db

class Person(db.Model):
  __tablename__ = 'person'
  person_id = db.Column(db.Integer, primary_key=True)
  lname = db.Column(db.String(32), index=True)
  fname = db.Column(db.String(32))
  timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  notes = db.relationship(
    'Note',
    backref='person',
    cascade='all, delete, delete-orphan',
    single_parent=True,
    order_by='desc(Note.timestamp)'
  )
