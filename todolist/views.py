from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from .models import Notes
from . import db
import json
views = Blueprint("views",__name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("index.html",user=current_user)

@views.route("/todolist", methods=["POST","GET"])
def todolist():
    if request.method=="POST":
        task= request.form.get("note")
        if len(task)<1:
            flash("Your task is too short", category="error")
        else:
            new_task=Notes(task=task, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash("Your task added", category="success")        
    return render_template("todo.html", user=current_user)
@views.route("/delete-note", methods=["POST","GET"])
def delete_task():
    task= json.loads(request.data)
    note_id=task["note_id"]
    result=Notes.query.get(note_id)
    if result:
        if result.user_id== current_user.id:
            db.session.delete(result)
            db.session.commit()
            flash("Deleted success",category="success")
            return jsonify({"code":200})
            
