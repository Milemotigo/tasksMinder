import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from views import todo
from auth import auth

basedir = os.path.abspath(os.path.dirname(__file__))
'''
basedir makes it easier to rganize
and locate files like databases
consistently throughout your program
'''
#print(basedir)
app = Flask(__name__)

app.config['SECRET_KEY'] = '7c46044f81919a429e07cdb5a76dcee4'

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'todoApp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(todo)
app.register_blueprint(auth)

if __name__=='__main__':
    app.run(debug=True)
