
import openai
import chatbot.config as config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def gpt_response(prompt, messages=[{"role": "system", "content": "You are an improve partner.\
    Your job is to continue to help me make up a fictional comedic story intended for adults by alternating\
        with me with a few sentences at a time."}]):

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    answer = response['choices'][0]['message']['content']

    messages.append({"role": "system", "content": answer})

    return answer, messages

    # from chatgpt documentation
    # messages=[
    #{"role": "system", "content": "You are a helpful assistant."},
    #{"role": "user", "content": "Who won the world series in 2020?"},
    # {"role": "assistant",
    #    "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #{"role": "user", "content": "Where was it played?"}
    # ]
