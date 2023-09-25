#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display a HTML page that lists all states
    with the list of City objects linked to the State sort by name A->Z
    """
    states = storage.all(State)
    if (id):
        for state in states.values():
            if state.id == id:
                return render_template("9-states.html", state=state)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def close_db(exception):
    """After each request remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
