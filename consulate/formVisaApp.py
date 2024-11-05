from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Email, DataRequired

class visaApplicationForm(FlaskForm):
    passportNumber = IntegerField(
        label='Passport number:', 
        validators=[DataRequired()])
    emailAddress = StringField(
        label='Email:',
        validators=[Email(), DataRequired()])
    submit = SubmitField(label='submit')
   