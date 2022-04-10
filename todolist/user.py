from flask import Blueprint

user = Blueprint("user",__name__)

@user.route("/login")
def login():
    return "Login page"

@user.route("/logout")
def logout():
    return "Logout page"
        
@user.route("/signup")
def signup():
    return "Sign Up page"