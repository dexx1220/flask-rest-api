from models.person import Person
from config import db, ma
from marshmallow import fields
from .person_note import PersonNoteSchema

class PersonSchema(ma.ModelSchema):
  class Meta:
    model = Person
    sqla_session = db.session
  notes = fields.Nested(PersonNoteSchema, default=[], many=True)