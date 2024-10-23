from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class ConnexionForm(FlaskForm):
    emailAddress = StringField(
        label='Email address:', 
        validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='submit')