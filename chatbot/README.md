# chatbot

chatbot application for CITS3043
Team Members: Elliot Walker, Gianni Spadoni, and Mark McIntire

This project is a basic ChatGPT front end implemented according to the Project 2 spec sheet, using Flask, Bootstrap 5, JQuery, CSS, and OpenAI's gpt-3.5-turbo API for chat completion.

It makes use of ChatGPT's contextual hinting feature to setup a setting where ChatGPT is acting as an improv story telling partner, using the following prompt.

> You are an improv partner, known as James The Wise.
> Your job is to continue to help me make up a fictional comedic story intended for adults by alternating
> with me with a sentence or two at a time, using what I say as the basis for your reply.

It contains a login page, featuring login/signup/about panels, alongside accompanying error states.

A homepage featuring a chat that connects to ChatGPT, with continuous message history in the session and streamed responses to avoid long delays, implemented with AJAX and JS.
The chat is displayed in a text bubble like format, similar to text messages on a phone.

Finally, a history page that displays chats identified by the time they were started and the user's first message. This history can also be searched by any message sent inside by the user inside a chat, which will be displayed in the list of results after being inputted. They can then be clicked to display the full chat in the same format as the chat page.


To start it, first go to the config.py file and replace the "secret key" string under OPENAI_KEY with your personal openai API key. If you are unsure what your key is, you can login and find or generate keys at https://platform.openai.com/account/api-keys . Once you have that, simply run "python3 app.py" from the directory containing the app.py file. 

The app will begin running at http://localhost:5000/

To run the selenium tests, make sure to have installed the requirements, and make sure to have Google's chromedriver package installed and available in your $PATH.
If desired, you may be able to change the line "webdriver.Chrome()" to "webdriver.Firefox()", and make sure Mozilla's geckodriver package is installed in your $PATH instead.

The tests will test for protected endpoints, non-existing endpoint redirection, failed login and failed sign in attempts producing errors displaying corresponding tab panes (i.e, A failed sign up does not bring you to the login section), and finally a full test demo using randomly generated data to from signup -> login -> homepage, response -> check history for our demo message -> completion
