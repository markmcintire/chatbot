# Initialize Flask Application
from flask import Flask
from .database import db, login_manager
from .auth import auth
from .home import home, is_active
from .stream import stream
from .history import history

app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# This should be stored in an environment variable.
app.config["SECRET_KEY"] = "212af25dbb394c6282e6be9a6156f9e5"


# This registers all the blueprints with the app. The blueprints are basically namespaces.
app.register_blueprint(home)
app.register_blueprint(stream)
app.register_blueprint(history)
app.register_blueprint(auth)
login_manager.init_app(app)


# This creates the database if it doesn't already exist.
db.init_app(app)
with app.app_context():
    db.create_all()


# This sets up a small helper function in the jinja namespace to allow template generation access to the current page.
app.jinja_env.globals.update(is_active=is_active)
