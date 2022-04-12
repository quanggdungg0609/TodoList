from flask import Blueprint, render_template, request, flash, session
from flask.helpers import url_for
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from flask_login import login_user, login_required, logout_user, current_user
from todolist import views
from .models import Users, Notes
from . import db
user = Blueprint("user",__name__)

@user.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        
        user=Users.query.filter_by(user_name=username).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user, remember=True)
                session.permanent=True
                flash("Logged in success!",category="succces")
                return redirect(url_for("views.todolist"))
            else:
                flash("Wrong password, please check again",category="error")
        else:
            flash("User doesn't exist",category="error")

    return render_template("login.html",user=current_user)

@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.login"))

        
@user.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        email=request.form.get("email")
        username=request.form.get("username")
        password=request.form.get("password")
        confirm_password=request.form.get("confirm_password")
        
        user=Users.query.filter_by(email=email).first()
        if user:
            flash("User existed", category="error")
        elif len(email)<10:
            flash("Email must be greater than 10 characters",category="error")
        elif len(password)<6:
            flash("Password must be greater than 6 character",category="error")
        elif password!=confirm_password:
            flash("Password doesn't not match", category="error")
        else:
            password=generate_password_hash(password, method="sha256")
            new_user=Users(email,username,password)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("User created!", category="success")
                login_user(user,remember=True)
                return redirect(url_for("views.home"))

            except:
                "Error"
    return render_template("signup.html",user=current_user)
