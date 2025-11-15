#!/usr/bin/python3
"""
task_04_flask.py

Sadə Flask API nümunəsi. `/hello` endpoint-i GET sorğularını qəbul edir
və JSON cavab qaytarır.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# GET endpoint
@app.route("/hello", methods=["GET"])
def hello():
    """Salam mesajı qaytarır"""
    return jsonify({"message": "Salam, Flask API işləyir!"})

# POST endpoint
@app.route("/echo", methods=["POST"])
def echo():
    """
    Göndərilən JSON məlumatını geri qaytarır.
    Məsələn: {"text": "Salam"} → {"echo": "Salam"}
    """
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "JSON-də 'text' açarı yoxdur"}), 400
    return jsonify({"echo": data["text"]})

if __name__ == "__main__":
    # Serveri localhost:5000 ünvanında işə salır
    app.run(host="0.0.0.0", port=5000, debug=True)
