import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from .views import todo
from .auth_app.auth import auth
from flask_bcrypt import Bcrypt


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    bcrypt = Bcrypt()
    basedir = os.path.abspath(os.path.dirname(__file__))
    '''
    basedir makes it easier to organize
    and locate files like databases
    consistently throughout your program
    '''
    app.config['SECRET_KEY'] = '7c46044f81919a429e07cdb5a76dcee4'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'TaskMinder.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)

    #todo app blueprint register
    app.register_blueprint(todo)

    #auth app registration
    app.register_blueprint(auth)

    return app
