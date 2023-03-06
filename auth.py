from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from db import mongo

from models import User

auth = Blueprint("auth", __name__, template_folder="templates/auth")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        users = mongo.db.users

        user = users.find_one({"email": email})

        if user:
            hashed_password = user['password']
            if check_password_hash(hashed_password, password):
                user = User(user)
                login_user(user, remember=True)
                return redirect(url_for("views.index"))
            else:
                return "Incorrect password, try again."
        else:
            return "User does not exist"
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        email = request.form["email"]

        existing_email = mongo.db.users.find_one({"email": email})
        if existing_email:
            print("email!!!!!", email)
            return 'That Email already exists'

        existing_email = mongo.db.users.find_one(
            {"email": email}
        )

        if existing_email is None:
            if not request.form["password1"] == request.form["password2"]:
                return "Password did not match"

            mongo.db.users.insert_one(
                {
                    "email": request.form["email"],
                    "first_name": request.form["first_name"],
                    "last_name": request.form["last_name"],
                    "password": generate_password_hash(request.form["password1"]),
                }
            )
            return redirect(url_for("views.index"))

        return "That email already exists"
    return render_template("signup.html", user=current_user)
