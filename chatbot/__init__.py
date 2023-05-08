# Initialize Flask Application
from flask_login import LoginManager
from flask import Flask
from .database import db, login_manager
from .auth import auth
from .home import home

app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "212af25dbb394c6282e6be9a6156f9e5"
app.register_blueprint(auth)
app.register_blueprint(home)


login_manager.init_app(app)

db.init_app(app)
with app.app_context():
    db.create_all()


