from flask import Blueprint, render_template
from flask_login import login_required, current_user

from db import mongo

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def index():
    return render_template("home.html", user=current_user)


@views.route("/users")
def users():
    users = mongo.db.users.find()
    return render_template("users.html", users=users, user=current_user)
