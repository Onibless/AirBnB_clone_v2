#!/usr/bin/python3
"""
A script that satarts a flask web application
"""
from flask import Flask
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
