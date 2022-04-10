from logging import NOTSET
from flask import Flask
import os
from dotenv import load_dotenv
from .user import user
from .views import views
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
load_dotenv()
SECRET_KEY=os.environ.get("SECRET_KEY")
DB_NAME= os.environ.get("DB_NAME")


def create_database(app):
    if not os.path.exists('todolist/'+DB_NAME):
        db.create_all(app=app)
        print("DB Created")
        
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=SECRET_KEY
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    #setting database
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{DB_NAME}"
    db.init_app(app)
    from .models import Notes,Users
    create_database(app)
    
    #Register blueprint
    app.register_blueprint(user)
    app.register_blueprint(views)
    return app