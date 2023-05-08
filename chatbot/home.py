from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required

home = Blueprint('home', __name__)

@home.route('/home')
@login_required
def homepage():
    return "Hello world!"