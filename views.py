from flask import Blueprint, render_template

todo = Blueprint('todo', __name__)

@todo.route('/todo')
def tasks():
    return render_template('index.html')

@todo.route('/notifications')
def notifications():
    return render_template('notifications.html')

@todo.route('/revenue')
def revenue():
    return render_template('revenue.html')

@todo.route('/analytics')
def analytics():
    return render_template('analytics.html')

@todo.route('/notes')
def notes():
    return render_template('notes.html')

@todo.route('/wallets')
def wallets():
    return render_template('wallets.html')

