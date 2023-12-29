#!/usr/bin/python3
""" Script to start a Flask web app
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def Hello_HBNB():
    return "Hello HBNB!"

@app.route("/hbnb")
def HBNB():
    return "HBNB!"

@app.route("/c/<text>")
def C_is_fun():
    return f'C {escape(text)}'
