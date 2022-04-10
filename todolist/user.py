from flask import Blueprint, render_template

user = Blueprint("user",__name__)

@user.route("/login")
def login():
    return render_template("login.html")

@user.route("/logout")
def logout():
    return "logout"

        
@user.route("/signup")
def signup():
    return render_template("signup.html")
