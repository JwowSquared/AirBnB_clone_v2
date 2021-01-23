#!/usr/bin/python3
"""x"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def a():
    """x"""
    states = []
    raw = storage.all("State").values()
    for state in raw:
        states.append({state.id: state.name})
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def b(err):
    """x"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
