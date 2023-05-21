from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin, LoginManager

import base64
import uuid


# module init, login view registration.
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
db = SQLAlchemy()


# This function simply retrieves the password hash and compares the incoming hash against it.
# If successful, it'll return the user model.
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None


# This is model represents a single message.
# The id is not used anywhere, but the module SQLAlchemy requires a primary key, when in practice it isn't needed.
class MessageRecord(db.Model):
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String)
    chat_id = db.Column(db.String)
    index = db.Column(db.Integer)
    role = db.Column(db.String)
    message = db.Column(db.String)
    created_at = db.Column(db.DateTime)


# Constructor for the message model.
def new_msg_record(user_id, chat_id, index, role, message):
    record = MessageRecord(
        id=str(uuid.uuid4()),
        user_id=user_id,
        chat_id=str(chat_id),
        index=index,
        role=role,
        message=message,
        created_at=func.now()
    )
    db.session.add(record)
    db.session.commit()


# This model represents a user, and inherits from Flask-Login's UserMixin.
# It also contains the function to check the password hash.
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def check_password(self, password):
        return check_password_hash(base64.b64decode(self.password.encode()).decode(), password)


# This is the constructor for the user model.
# User ID is a universal unique idenitifer.
# Base64 encoded passwords so they can just be strings.
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


# Returns a user from the database by ID.
# Registered with Flask-Login so its functions know what to call.
@login_manager.user_loader
def find_user_by_id(user_id):
    return User.query.get(user_id)


# This retrieves by username.
# It's used to login, usernames have to be unique so need to worry about a collision.
def retrieve_user(username):
    return User.query.filter_by(username=username).first()
