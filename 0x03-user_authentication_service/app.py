#!/usr/bin/env python3
""" The flask application for the app
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome() -> str:
    """ Return a payload
    """
    message = {"message": "Bienvenue"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
