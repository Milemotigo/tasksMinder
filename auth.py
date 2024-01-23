from flask import Blueprint, render_template, request, redirect, flash
from . forms import RegistrationForm, LoginForm
from . views import *



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    ''''''
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'invalid username/password'
    return render_template('auth/auth.html', error=error)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    ''''''
    form = forms.RegistrationForm()
    
    if form.valid_on_submit():
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('auth/auth.html', title='Register', form='form')

