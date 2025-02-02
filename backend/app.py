from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from ai_model import ask_ai

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AI Python Tutor Backend is Running!"})


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("message", "")
    response = ask_ai(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
