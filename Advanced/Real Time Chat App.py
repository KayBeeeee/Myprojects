"""
Real-Time Chat Application with WebSockets and NLP Integration
-------------------------------------------------------------
This script sets up a real-time chat server using Flask-SocketIO and integrates NLP
for message sentiment analysis and chatbot responses.

Libraries:
- Flask-SocketIO for real-time communication
- spaCy for sentiment analysis
- Flask for routing

Steps:
1. Set up WebSocket communication between clients.
2. Analyze message sentiment using spaCy.
3. Use a simple chatbot to respond to messages.
"""

import spacy
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from textblob import TextBlob

# Initialize Flask app and Flask-SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Load the spaCy model for sentiment analysis
nlp = spacy.load("en_core_web_sm")

# Simple chatbot function
def simple_chatbot(message):
    # Basic rule-based chatbot
    if "hello" in message.lower():
        return "Hello! How can I assist you today?"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm here to help you!"

# Sentiment analysis using spaCy
def analyze_sentiment(message):
    doc = nlp(message)
    sentiment = doc.sentiment
    return "Positive" if sentiment >= 0 else "Negative"

# Route for the chat page
@app.route('/')
def index():
    return render_template('chat.html')

# WebSocket communication
@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")

    # Analyze sentiment
    sentiment = analyze_sentiment(message)
    print(f"Sentiment: {sentiment}")

    # Get a response from the chatbot
    response = simple_chatbot(message)

    # Send the sentiment and response back to the client
    send({"sentiment": sentiment, "response": response}, broadcast=True)

# Run the Flask-SocketIO app
if __name__ == '__main__':
    socketio.run(app, debug=True)
