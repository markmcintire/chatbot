from flask import Blueprint, Response, request, stream_with_context, session, g
from flask_login import login_required, current_user
from .messages import MessagesHistory, construct_history
from .database import MessageRecord, new_msg_record
import uuid
import openai
import chatbot.config as config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

stream = Blueprint('stream', __name__)


# This is code to stream a ChatGPT response while collecting the chunks in a string, and then store that string in the database with its application specific metadata.
# It uses a message history retrieved from the database using the current chat_id, which specifies the context.
def chat_gpt_response(messages, user_id):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        stream=True  # this time, we set stream=True
    )
    reply = ""
    for chunk in response:
        if chunk['choices'][0]['finish_reason'] is None:
            if chunk['choices'][0]['delta'].get('content', None) is not None:
                reply += chunk['choices'][0]['delta']['content']
                yield chunk['choices'][0]['delta']['content']
        else:
            new_msg_record(
                user_id, session['chat_id'], session['chat_index'], 'assistant', reply)
            return "Fin"

# This function handles setting up the application metadata for the chat messages, and then calling the message history constructor with it.


@stream.route('/stream', methods=["POST"])
@login_required
def stream_it():
    request_data = request.json
    user_id = current_user.get_id()
    if request_data['new_chat']:
        session['chat_id'] = uuid.uuid4()
        session['chat_index'] = 0
    else:
        session['chat_index'] += 1
    new_msg_record(
        user_id, session['chat_id'], session['chat_index'], 'user', request_data['input'])
    messages = construct_history(session['chat_id']).messages
    print(messages)
    return Response(stream_with_context(chat_gpt_response(messages, user_id)), mimetype='text/event_stream', status=200)
