#!/usr/bin/python3
""" Script to start a Flask web app
"""
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def Hello_HBNB():
    """ route to display 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """ route to display 'HBNB!'
    """
    return "HBNB!"


@app.route("/c/<text>")
def C_is_fun(text="is cool"):
    """ route that displays c and the string int the <text> variable
    """
    return f'C {escape(text)}'


@app.route("/python/<text>")
def Python(text="is cool"):
    """ route that displays 'Python' and the string in the <text> variable
    """
    return f'C {escape(text)}'

if __name__ == '__main__':
    """ Prevents execution when imported"""
    app.run(host='0.0.0.0', port=5000)
