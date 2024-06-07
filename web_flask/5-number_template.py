#!/usr/bin/python3
""" script that start a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ return Hello HBNB! """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return Hello HBNB! """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ serves content to /c/<text> """
    return "C " + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """ serves content to /python/<text> """
    return "python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ serves content to /python/<text> """
    return str(n) + " is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ serves content to /python/<text> """
    return render_template('5-number_template.html', n=n)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
