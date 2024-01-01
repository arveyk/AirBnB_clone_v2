#!/usr/bin/python3
from flask import Flask
""" Module to start a Flask web app
"""

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def Hello_HBNB():
    return "Hello HBNB!"
