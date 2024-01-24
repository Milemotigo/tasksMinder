from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(min=15, max=23)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('Email', validators=[DataRequired(), Length(min=6, max=200)])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Sign Up')

