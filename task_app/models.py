from ..api.app import db
from flask_login import UserMixin
from datetime import datetime
from ..auth_app.models import User
from ..utils.enums import Priority
from enum import Enum

class Task(UserMixin, db.Models):
    '''tasks models'''
    __tablename__='task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    discription = db.Column(db.Text())
    start = db.Column(db.DateTime, default=datetime.utcnow)
    expires = db.Column(db.DateTime, default=datetime.utcnow)
    priority = db.Column(db.Enum(Priority), default=Priority.low)
    
    user_id = db.Column(db.Integer, ForiegnKey(user.id))


