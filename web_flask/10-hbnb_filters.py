#!/usr/bin/python3
"""x"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def a():
    """x"""
    s = storage.all("State").values()
    a = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html", states=s, amenities=a)


@app.teardown_appcontext
def b(err):
    """x"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
