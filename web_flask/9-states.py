#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_list(state_id=None):
    """
        display a HTML page insstate_ide BODY
            H1 -> states
            UL -> list of all State 
                LI -> <state.state_id>: <B><state.name></B>
    """
    states = storage.all(State)
    if state_id:
        state_id = 'State.' + state_id
        if state_id not in states.keys():
            state_id = None

    return render_template('9-states.html', states=states, state_id=state_id)

@app.teardown_appcontext
def teardown_session(exception):
    """ remove the current sqlalchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
