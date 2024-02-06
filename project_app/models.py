from ..api.app import db
from flask_login import UserMixin
from datetime import datetime
from ..auth_app.models import User
from ..enum.utils import Priority
from enum import Enum

class Project(UserMixin, db.Models):
    '''tasks models'''
    __tablename__='task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    discription = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    start = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ends = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utc.now)
    priority = db.Column(db.Integer)
    colaborators = db.Column()
    published

    user_id = db.Column(db.Integer, db.ForiegnKey(user.id))
