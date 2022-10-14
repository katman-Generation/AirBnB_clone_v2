#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Return a string at the root route"""
    return 'HELLO HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string at the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns a string at the /c/<text> route,
    expanda the <text> variable"""
    new = text.replace('_', ' ')
    return 'C %s' % new


if __name__ == '__main__':
    app.run(host='0.0.0.0')
