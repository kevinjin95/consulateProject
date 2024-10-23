from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    email = StringField(
        label='Email:',
        validators=[Email(), DataRequired()])
    password1 = StringField(
        label='Password:',
        validators=[Length(min=16), DataRequired()])
    password2 = StringField(
        label='Confirm password:', 
        validators=[EqualTo('password1'), DataRequired()])
    firstName = StringField(label='First name:', validators=[DataRequired()])
    name = StringField(label='Name:', validators=[DataRequired()])
    age = StringField(label='Age:')
    doorNumber = StringField(label='Door number:')
    road = StringField(label='Road:')
    city = StringField(label='City:')
    postalCode = StringField(label='Postal code :')
    phoneNumber = StringField(label='Phone number')
    passportNumber = StringField(label='Passport number:')
    passportExpDate = StringField(label='Passport expiration date:')
    passportCreDate = StringField(label='Passport creation date:')
    submit = SubmitField(label='submit')