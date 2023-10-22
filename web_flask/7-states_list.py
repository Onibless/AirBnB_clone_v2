#!/usr/bin/python3
from flask import Flask, render_template
# from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", stirct_slashes=False)
def states_list():
    """Fetches state table data"""
    states = storage.all()
    return(render_template('7-states_list.html', state=states))


@app.teardown_appcontext
def teardown(self):
    """closes sqlalchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
