from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

history = Blueprint('history', __name__)


@history.route('/history', methods=["POST", "GET"])
@login_required
def historypage():
    return render_template('history.html')
