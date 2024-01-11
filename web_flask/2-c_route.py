#!/usr/bin/python3
""" Script to start a Flask web app
"""
from flask import Flask
from markupsafe import escape

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
    return "HBNB"


@app.route("/c/<text>")
def C_is_fun(text):
    """ route that displays c and the string int the <text> variable
    """
    text2 = ""
    char_len = 0
    if (text):
        while char_len < len(text):
            if text[char_len] == '_':
                text2 += ' '
            else:
                text2 += text[char_len]
            char_len += 1

    return f'C {escape(text2)}'


if __name__ == '__main__':
    """ Prevents execution when imported"""
    app.run(host='0.0.0.0', port=5000)
