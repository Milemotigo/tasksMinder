from flask import Blueprint, render_template, request, redirect, flash
#from . forms import RegistrationForm, LoginForm
#from . views import *


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('Email', validators=[DataRequired(), Length(min=6, max=200)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign Up')

auth = Blueprint('auth', __name__)

@auth.route('/')
def dashboard():
    return render_template('dashboard.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    ''''''
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'Login successfully for {form.username.data}!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('auth/login.html', title='Register', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    ''''''
    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('views.notes'))
    return render_template('auth/signup.html', title='Register', form=form)

