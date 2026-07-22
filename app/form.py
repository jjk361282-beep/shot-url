from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField
from wtforms.validators import Length,DataRequired,ValidationError
from .model import User
from .db import db
import sqlalchemy as sa

class LoginUser(FlaskForm):
    name=StringField(label="UserName",validators=[DataRequired()])
    email=EmailField(validators=[DataRequired()])
    password=PasswordField(validators=[DataRequired(),Length(min=8)])

    # def validate_email(self,email):
    #     user=db.session(sa.select(User).where(
    #         User.email==email.data
    #     ))
    #     if user is not None:
    #         raise ValidationError

class SignUser(FlaskForm):
    email=EmailField(validators=[DataRequired()])
    password=PasswordField(validators=[DataRequired()])