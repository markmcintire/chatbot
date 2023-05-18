from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required

search = Blueprint('search', __name__)


@search.route('/search', methods=["POST", "GET"])
@login_required
def searchpage():
    return render_template('search.html')
