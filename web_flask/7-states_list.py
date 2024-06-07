#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
        display a HTML page inside BODY
            H1 -> states
            UL -> list of all State 
                LI -> <state.id>: <B><state.name></B>
    """
    states = [state.to_dict() for state in storage.all(State).values()]
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_session(exception):
    """ remove the current sqlalchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
