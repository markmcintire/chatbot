from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

home = Blueprint('home', __name__)


@home.route('/home', methods=["POST", "GET"])
@login_required
def homepage():
    return render_template('home.html')


@home.route('/search')
@login_required
def search():
    return render_template('search.html')


# navbar


def is_active(url):
    if (url == request.path):
        return 'active'
    else:
        return ''
