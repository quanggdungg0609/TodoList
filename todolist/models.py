from datetime import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Notes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(1000000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(1500))
    user_name =  db.Column(db.String(20))
    notes = db.relationship("Notes")
    
    def __init__(self, email, user_name,password):
        self.email=email
        self.user_name=user_name
        self.password=password
        
