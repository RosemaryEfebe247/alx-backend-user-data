#!/usr/bin/env python3
""" The flask application for the app
"""
from auth import Auth
from flask import Flask, jsonify, request


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome() -> str:
    """ Return a payload
    """
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ The endpoint for User registration
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        register = AUTH.register_user(email, password)
        message = {"email": email, "message": "user created"}
        return jsonify(message)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
