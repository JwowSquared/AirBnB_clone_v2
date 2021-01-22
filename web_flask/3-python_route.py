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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """x"""
    return "C {}".format(text).replace("_", " ")


@app.route("/python", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def d(text):
    """x"""
    return "Python {}".format(text).replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
