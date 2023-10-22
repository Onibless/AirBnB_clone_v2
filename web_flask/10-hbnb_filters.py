#!/usr/bin/python3
"""importing flask module
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """fetches state from databse
    """
    states = State.all("State")
    amenities = State.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def tear_down():
    """closes sqlalchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
