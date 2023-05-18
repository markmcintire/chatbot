from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .chat import gpt_response

home = Blueprint('home', __name__)


@home.route('/home', methods=["POST", "GET"])
@login_required
def homepage():

    if request.method == "POST":
        prompt = request.form['prompt']
        answer = gpt_response(prompt)
        
        print(current_user)

        res = {}
        res['answer'] = answer
        return jsonify(res), 200

    return render_template('home.html')
