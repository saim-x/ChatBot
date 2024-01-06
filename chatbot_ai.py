
# chatbot_ai.py
import google.generativeai as palm

class Chatbot:
    def __init__(self):
        API_KEY = "AIzaSyDouqB56L-MU831RWff2SKSydGjad2wrfA"
        palm.configure(api_key=API_KEY)

        examples = [
            ('Hello, how can i be your assistant?', 'I need help with my university studies.'),
        ]

        self.response = palm.chat(
            messages="I need help in my universities studies, Can you help me pls",
            temperature=0.8,
            context='Speak like a professor',
            examples=examples,
        )

    def generate_response(self, user_input):
        # Handle user input and generate a response using the chatbot logic
        self.response = self.response.reply(user_input)
        return self.response.last
