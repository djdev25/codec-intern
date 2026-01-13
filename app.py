from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from database import create_table, save_chat

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    bot_msg = get_response(user_msg)
    save_chat(user_msg, bot_msg)
    return jsonify({"response": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
