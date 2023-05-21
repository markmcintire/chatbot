from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func, literal

from chatbot.database import MessageRecord

history = Blueprint('history', __name__)


@history.route('/history', methods=["POST", "GET"])
@login_required
def historypage():
    return render_template('history.html')


@history.route('/search', methods=["POST"])
@login_required
def search():
    request_data = request.json
    query_text = request_data["query"]  # Simple string query

    # Let's find conversations (or "prompts") with the query
    query_result = MessageRecord.query \
        .filter(func.lower(MessageRecord.message).contains(func.lower(literal(query_text)))) \
        .filter(MessageRecord.role == "user") \
        .group_by(MessageRecord.chat_id)

    response_dict = {"result": []}

    for record in query_result:
        response_dict["result"].append({
            "message": record.message,
            "chat_id": record.chat_id,
            "created_at": record.created_at
        })

    return jsonify(response_dict)
