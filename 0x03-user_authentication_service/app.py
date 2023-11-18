#!/usr/bin/env python3
""" The flask application for the app
"""
from flask import abort, Flask, jsonify, request

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ Return a payload
    """
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ POST /users
    Return:
        - The user payload
    """
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        register = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ The login endpoint. Returns Session payload
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password) is False:
        abort(401)
    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
