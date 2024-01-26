from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm, RegistrationForm
from .utils import split_email

auth = Blueprint('auth', __name__)
#auth = create_app()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        email_prefix = split_email(email)
        flash(f'Login successfully for {email_prefix}!', 'success')
        return redirect(url_for('todo.dashboard'))
    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print('success')
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('todo.dashboard'))
    else:
        print(' not valid reg ')
    return render_template('auth/register.html', title='Register', form=form)

@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('auth/forgot-password.html')

