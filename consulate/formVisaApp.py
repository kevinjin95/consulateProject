from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class visaApplicationForm(FlaskForm):
    passportNumber = StringField(label='Passport number:')
    emailAddress = StringField(
        label='Email:',
        validators=[Email(), DataRequired()])
    submit = SubmitField(label='submit')
   