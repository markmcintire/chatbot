from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .chat import gpt_response
from .database import new_record

home = Blueprint('home', __name__)


@home.route('/home', methods=["POST", "GET"])
@login_required
def homepage():
    if request.method == "POST":

        prompt = request.form['prompt']

        try:
            answer, messages = gpt_response(prompt, messages)
        except:
            answer, messages = gpt_response(prompt)

        new_record(current_user.id, prompt, answer)

        res = {}
        res['answer'] = answer
        return jsonify(res), 200

    return render_template('home.html')


@home.route('/history')
@login_required
def history():
    return render_template('history.html')

# navbar


def is_active(url):
    if (url == request.path):
        return 'active'
    else:
        return ''
