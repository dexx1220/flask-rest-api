from config import ma
from marshmallow import fields

class PersonNoteSchema(ma.ModelSchema):
  note_id = fields.Int()
  person_id = fields.Int()
  content = fields.Str()
  timestamp = fields.Str()