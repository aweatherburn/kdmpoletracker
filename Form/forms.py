from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class ContactForm(FlaskForm):
    name = StringField('NAME', validators=[DataRequired('A full name is required'), Length(min=5, max=30)])
    email = StringField('EMAIL', validators=[DataRequired('A correct email is required'), Email()])
    message = TextAreaField('MESSAGE', validators=[DataRequired('A message is required'), Length(min=5, max=500)])
    submit = SubmitField('SEND')

class DataForm(FlaskForm):
    location = StringField('LOCATION', validators=[DataRequired('Enter a LOC #'), Length(min=1, max=6)])
    comEd = StringField('COMED', validators=[DataRequired('Enter a ComEd #'), Length(min=1, max=10)])
    ike = StringField('IKE', validators=[DataRequired('Enter a ComEd #'), Length(min=1, max=10)])
    kmz = StringField('KMZ', validators=[DataRequired('Enter a ComEd #'), Length(min=1, max=10)])
    coordinates = StringField('COORDINATES', validators=[DataRequired('Enter a ComEd #'), Length(min=1, max=30)])
    fiber_bundle = StringField('FIBER_BUNDLE', validators=[DataRequired('Enter a ComEd #'), Length(min=1, max=30)])
    submit = SubmitField('ADD NEW LOC')