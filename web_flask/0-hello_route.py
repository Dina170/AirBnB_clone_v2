#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    """Displays 'Hello HBNB!'
    """
    app.run(debug=True, port=5000, host="0.0.0.0")
