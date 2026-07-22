from apiflask import Schema
from apiflask.fields import String,Email
from apiflask.validators import Length

class UserSchema(Schema):
    name=String(required=True)
    email=Email(required=True)
    password=String(Length)