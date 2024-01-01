#!/usr/bin/python3
""" Module to start a Flask Web app
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def Hello_HBNB():
    """ Route to display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """ Route to display 'HBNB!'"""
    return "HBNB!"
