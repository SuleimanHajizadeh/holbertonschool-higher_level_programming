#!/usr/bin/python3
"""
task_05_basic_security.py

Sadə token əsaslı API təhlükəsizliyi nümunəsi.
"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sadə API token
API_TOKEN = "holberton123"

def token_required(f):
    """Decorator: Token yoxlanışı"""
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != f"Bearer {API_TOKEN}":
            # İcazəsiz giriş
            abort(401, description="Unauthorized: Yanlış və ya yoxsuz token")
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# Təhlükəsiz endpoint
@app.route("/secure-data", methods=["GET"])
@token_required
def secure_data():
    """Token doğrulandısa məlumat qaytarır"""
    return jsonify({"data": "Bu məlumat yalnız səlahiyyətli istifadəçilər üçündür."})

if __name__ == "__main__":
    # Serveri localhost:5000 ünvanında işə salır
    app.run(host="0.0.0.0", port=5000, debug=True)
