from models.note import Note
from config import db, ma
from marshmallow import fields
from .person import PersonSchema

class NoteSchema(ma.ModelSchema):
  class Meta:
    model = Note
    sqla_session = db.session
  person = fields.Nested(PersonSchema, exlcude=["notes"])