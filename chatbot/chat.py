
import openai
import chatbot.config as config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def gpt_response(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are an assistant"})
    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    answer = response['choices'][0]['message']['content']

    return answer

    # from chatgpt documentation
    # messages=[
    #{"role": "system", "content": "You are a helpful assistant."},
    #{"role": "user", "content": "Who won the world series in 2020?"},
    # {"role": "assistant",
    #    "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #{"role": "user", "content": "Where was it played?"}
    # ]
