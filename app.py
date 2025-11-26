from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Simple rule-based chatbot
def chatbot_response(message):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! How can I assist you?"

    elif "your name" in msg:
        return "I'm WebChat — your virtual assistant!"

    elif "time" in msg:
        now = datetime.datetime.now()
        return "The current time is " + now.strftime("%I:%M %p")

    elif "how are you" in msg:
        return "I'm great! Ready to help you. 😊"

    elif "bye" in msg:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I didn't understand that. Try asking something else."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form["msg"]
    return chatbot_response(user_msg)

if __name__ == "__main__":
    app.run(debug=True)
