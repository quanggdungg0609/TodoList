from logging import NOTSET
from flask import Flask
import os
#from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from datetime import timedelta

db=SQLAlchemy()
#load_dotenv()
#SECRET_KEY=os.environ.get("SECRET_KEY")
#DB_NAME= os.environ.get("DB_NAME")


def create_database(app):
    if not os.path.exists('todolist/todolist.db'):
        db.create_all(app=app)
        print("DB Created")
        
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="todolist"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    #setting database
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///todolist.db"
    db.init_app(app)
    
    from .models import Notes,Users
    create_database(app)
    from .user import user
    from .views import views
    
    #Register blueprint
    app.register_blueprint(user)
    app.register_blueprint(views)
    
    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)
    app.permanent_session_lifetime=timedelta(minutes=1)
      
      
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))
    
    return app