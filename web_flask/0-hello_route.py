#!/usr/bin/python3
""" Module to start a Flask web app
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def Hello_HBNB():
    """
    Route to dispay 'Hello HBNB'
    """
    return "Hello HBNB!"
