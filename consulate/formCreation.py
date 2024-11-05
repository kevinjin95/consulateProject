from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    userName = StringField(
        label='userName:', 
        validators=[DataRequired(), Length(min=2, max=30)])
    emailAddress = StringField(
        label='Email:',
        validators=[Email(), DataRequired(), Length(max=40)])
    password1 = PasswordField(
        label='Password:',
        validators=[Length(min=16), DataRequired(), Length(max=80)])
    password2 = PasswordField(
        label='Confirm password:', 
        validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='submit')