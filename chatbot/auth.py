from flask import Blueprint
auth = Blueprint('auth', __name__)

#placeholder
@auth.route('/login')
def login():
        return "Hello world!"
