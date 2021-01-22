#!/usr/bin/python3
"""x"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def e(n):
    """x"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def f(n):
    """x"""
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def g(n):
    """x"""
    out = "odd"
    if n % 2 == 0:
        out = "even"
    out = "{:d} is {}".format(n, out)
    return render_template("6-number_odd_or_even.html", num=out)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
