#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def Hello_HBNB():
    return "<p>Hello HBNB!</p>"

@app.route("/hbnb")
def Hello_HBNB():
    return "<p>HBNB!</p>"
