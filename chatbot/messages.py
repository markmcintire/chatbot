from .database import MessageRecord


class MessagesHistory:
    def __init__(self):
        self.messages = [{"role": "system", "content": "You are an improv partner, known as James The Wise.\
    Your job is to continue to help me make up a fictional comedic story intended for adults by alternating\
        with me with a sentence at a time."}, {"role": "assistant", "content": "Greetings, my dear friend! Are you ready for a wild and hilarious adventure?"}]

    def insert_user_input(self, prompt):
        question = {}
        question['role'] = 'user'
        question['content'] = prompt
        self.messages.append(question)

    def insert_gpt_reply(self, text):
        reply = {}
        reply['role'] = 'assistant'
        reply['content'] = text
        self.messages.append(reply)


def construct_history(chat_id):
    history = MessagesHistory()
    list = MessageRecord.query.filter_by(
        chat_id=str(chat_id)).all()
    for record in list:
        if (record.role == 'assistant'):
            history.insert_gpt_reply(record.message)
        else:
            history.insert_user_input(record.message)
    return history
