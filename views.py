from flask import Blueprint, render_template
#from app import create_app
todo = Blueprint('todo', __name__)
#todo = create_app()

@todo.route('/')
def dashboard():
    return render_template('dashboard.html')

@todo.route('/notifications')
def notifications():
    print('here')
    return render_template('topNav/notifications.html')

@todo.route('/revenue')
def revenue():
    return render_template('revenue.html')

@todo.route('/analytics')
def analytics():
    return render_template('analytics.html')

#@todo.route('/notes')
#def notes():
#    return render_template('cards.html')

@todo.route('/wallets')
def wallets():
    return render_template('cards.html')

