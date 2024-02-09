from flask import Blueprint

jquery = Blueprint('test', __name__)

@test.route('jquery')
def learn():
    '''learning app'''

