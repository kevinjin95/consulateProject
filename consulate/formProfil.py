from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class ProfilForm(FlaskForm):
    userName = StringField(
        label='userName:', 
        validators=[DataRequired(), Length(min=2, max=30)])
    emailAddress = StringField(
        label='Email:',
        validators=[Email(), DataRequired(), Length(max=40)])
    password1 = PasswordField(
        label='Password:',
        validators=[Length(min=6, max=80), DataRequired()])
    password2 = PasswordField(
        label='Confirm password:', 
        validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Modify')