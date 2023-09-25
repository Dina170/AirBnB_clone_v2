#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page that lists all states
    with the list of City objects linked to the State sort by name A->Z
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(exception):
    """After each request remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
