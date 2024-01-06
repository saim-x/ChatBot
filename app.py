
# app.py
from gevent.pywsgi import WSGIServer
from flask import Flask, render_template, request
from chatbot_ai import Chatbot
import os

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

http_server = WSGIServer(('', int(os.environ.get('PORT', 5000))), app)
http_server.serve_forever()





