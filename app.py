
# app.py
from flask import Flask, render_template, request
from chatbot_ai import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')

    bot_response = chatbot.generate_response(user_input)
    

    return render_template('index.html', user_input=user_input, bot_response=bot_response)

@app.route('/reset')
def reset():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




