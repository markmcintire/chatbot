from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
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
    prompt = db.Column(db.String)
    response = db.Column(db.String)
    created_at = db.Column(db.DateTime)


class MessageRecord(db.Model):
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String)
    chat_id = db.Column(db.String)
    index = db.Column(db.Integer)
    role = db.Column(db.String)
    message = db.Column(db.String)


def new_msg_record(user_id, chat_id, index, role, message):
    record = MessageRecord(
        id=str(uuid.uuid4()),
        user_id=user_id,
        chat_id=str(chat_id),
        index=index,
        role=role,
        message=message
    )
    db.session.add(record)
    db.session.commit()


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


def new_record(user_id, prompt, response):
    record = ChatRecord(
        user_id=user_id,
        prompt=prompt,
        response=response,
        created_at=func.now()
    )
    db.session.add(record)
    db.session.commit()


@login_manager.user_loader
def find_user_by_id(user_id):
    return User.query.get(user_id)


def retrieve_user(username):
    return User.query.filter_by(username=username).first()
