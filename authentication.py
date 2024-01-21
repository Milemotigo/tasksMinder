from flask import Blueprint, render_template, request

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
    return render_template('auth/login.html', error=error)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    ''''''
    error = None
    fullname=email=password1=password2=profile_photo=''
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        profile_photo = request.form['profile_photo']
        if valid_signup(username, email, password1, password2):
            return signup_the_user_in(fullname, email, password1)
        else:
            error = 'invalid username/password'
    context = {
            'error':error,
            'fullname':fullname,
            'email':email,
            'password1':password1,
            'password2':password2,
            'profile_photo':profile_photo
            }
    return render_template('auth/signup.html', **context)
