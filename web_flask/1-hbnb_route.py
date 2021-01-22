#!/usr/bin/python3
"""x"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def a():
    """x"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def b():
    """x"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
