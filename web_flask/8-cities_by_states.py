#!/usr/bi/python3
"""Fetches state data from database"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Fetches states and cities"""
    states = storage.all()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Closes all sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
