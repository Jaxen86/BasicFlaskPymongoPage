from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
import os
from db import mongo
from models import User

load_dotenv()

# Initialize application
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Initialize the database
database_url = os.getenv("DATABASE_FULL")
app.config["MONGO_URI"] = database_url
mongo.init_app(app)

# Routes
from auth import auth
from views import views

app.register_blueprint(auth)
app.register_blueprint(views)

# login manager
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
    u = mongo.db.users.find_one({"email": email})
    if not u:
        return None
    user = User(u)
    return user


if __name__ == "__main__":
    app.run(debug=True)
