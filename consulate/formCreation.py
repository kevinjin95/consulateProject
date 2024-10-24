from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    firstName = StringField(label='First name:', validators=[DataRequired()])
    name = StringField(label='Name:', validators=[DataRequired()])
    emailAddress = StringField(
        label='Email:',
        validators=[Email(), DataRequired()])
    password1 = PasswordField(
        label='Password:',
        validators=[Length(min=16), DataRequired()])
    password2 = PasswordField(
        label='Confirm password:', 
        validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='submit')