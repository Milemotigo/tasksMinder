from flask import Blueprint, render_template, flash, redirect, url_for
from forms import LoginForm, RegistrationForm
from utils import split_email

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        email_prefix = split_email(email)
        flash(f'Login successfully for {email_prefix}!', 'success')
        return redirect(url_for('todo.dashboard'))
    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.username.data is None:
        print('not found')
    if form.validate_on_submit():
        print(form.username)
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('todo.dashboard'))
    return render_template('auth/signup.html', title='Register', form=form)

