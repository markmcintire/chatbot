from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY
from flask_login import UserMixin, LoginManager
import base64
import uuid

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
db = SQLAlchemy()


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None


class ChatRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    text = db.Column(db.String)
    # maybe add a date here?


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def check_password(self, password):
        return check_password_hash(base64.b64decode(self.password.encode()).decode(), password)


def new_user(username, email, password):
    user = User(
        id=str(uuid.uuid4()),
        username=username,
        email=email,
        password=base64.b64encode(
            generate_password_hash(password).encode()).decode()
    )
    db.session.add(user)
    db.session.commit()


@login_manager.user_loader
def find_user_by_id(user_id):
    return User.query.get(user_id)


def retrieve_user(username):
    return User.query.filter_by(username=username).first()
