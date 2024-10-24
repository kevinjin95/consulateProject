from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class ProfilForm(FlaskForm):
    firstName = StringField(label='First name:', validators=[DataRequired()])
    name = StringField(label='Name:', validators=[DataRequired()])
    age = StringField(label='Age:')
    doorNumber = StringField(label='Door number:')
    road = StringField(label='Road:')
    city = StringField(label='City:')
    postalCode = StringField(label='Postal code:')
    phoneNumber = StringField(label='Phone number:')
    emailAddress = StringField(
        label='Email:',
        validators=[Email(), DataRequired()])
    
    password = PasswordField(
        label='Password:',
        validators=[Length(min=16), DataRequired()])
   
    submit = SubmitField(label='submit')