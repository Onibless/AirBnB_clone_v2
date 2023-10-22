#!/usr/bin/python3
"""fetches states from database"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state():
    """Fetches state data from database"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.rout('/states/<id>', strict_slashes=False)
def state_id(id):
    """Fetches states by id from the database"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state, mode='id')
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def close(self):
    """Closes all sqlalchemy sessions"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
