#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page that lists all states sort by name A->Z
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db(exception):
    """After each request remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
