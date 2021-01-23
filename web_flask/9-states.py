#!/usr/bin/python3
"""x"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states", defaults={"id": None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def a(id):
    """x"""
    s = storage.all("State").values()
    if id is None:
        s = storage.all("State").values()
        return render_template("9-states.html", states=s)
    for state in s:
        if state.id == id:
            c = storage.all("City").values()
            return render_template("9-states.html", states=state, cities=c)
    return render_template("9-states.html")


@app.teardown_appcontext
def b(err):
    """x"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
