from models import Person, Note
from config import db, ma
from marshmallow import fields

class PersonSchema(ma.ModelSchema):
  class Meta:
    model = Person
    sqla_session = db.session
  notes = fields.Nested('PersonNoteSchema', default=[], many=True)

class PersonNoteSchema(ma.ModelSchema):
  note_id = fields.Int()
  person_id = fields.Int()
  content = fields.Str()
  timestamp = fields.Str()

class NoteSchema(ma.ModelSchema):
  class Meta:
    model = Note
    sqla_session = db.session
  person = fields.Nested(PersonSchema, exlcude=["notes"])
