from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

home = Blueprint('home', __name__)


# Home route, renders the home.html, the javascript there does the real work.
@home.route('/home', methods=["POST", "GET"])
@login_required
def homepage():
    return render_template('home.html')


# The is active helper function, for working out the current page in jinja template generation.
def is_active(url):
    if url == request.path:
        return 'active'
    else:
        return ''
