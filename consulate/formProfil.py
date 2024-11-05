from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class ProfilForm(FlaskForm):
    firstName = StringField(label='First name:', validators=[DataRequired()])
    name = StringField(label='Name:')
    age = IntegerField(label='Age:')
    doorNumber = IntegerField(label='Door number:')
    road = StringField(label='Road:')
    city = StringField(label='City:')
    postalCode = IntegerField(label='Postal code:')
    phoneNumber = StringField(label='Phone number:')
    emailAddress = StringField(
        label='Email:',
        validators=[Email(), DataRequired(), Length(max=40)])
    password = PasswordField(
        label='Password:',
        validators=[Length(min=16), DataRequired()])
    modify = SubmitField(label='modify')