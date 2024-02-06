from ..api.app import db
from flask_login import UserMixin

class Plan(UserMixin, db.Model):
    '''plan models '''
    __tablename__ = 'plan'


    id = db.Column(db.integer, primary_key=True)

