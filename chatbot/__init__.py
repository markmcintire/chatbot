# Initialize Flask Application
from flask import Flask
from .database import db
from .auth import auth

app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.register_blueprint(auth)
db.init_app(app) # Initialize database
with app.app_context():
    db.create_all() # Create all, doesn't actually update tables if they exist, so make sure to drop them first.

