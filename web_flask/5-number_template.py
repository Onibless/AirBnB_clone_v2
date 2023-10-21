#!/usr/bin/python3
"""
A script that satarts a flask web application
"""
from flask import Flask
from flask import render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Function that returns a string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Function that returns a string
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Function that returns a string
    """
    str = text.replace("_", " ")
    return f"C {escape(str)}"


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Function that returns a string
    """
    str = text.replace("_", " ")
    return f"Python {escape(str)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Function that returns a string
    """
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Function that returns a string
    """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
