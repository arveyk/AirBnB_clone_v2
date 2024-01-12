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


@app.route("/python/<text>")
def Python(text="is cool"):
    """ route that displays 'Python' and the string in the <text> variable
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

    return f'Python {escape(text2)}'


@app.route("/number/<int:n>")
def number(n):
    """ route that displays in if and only if n is a number
    """
    return f'{escape(n)} is a number'


@app.route("/number_template/<int:n>")
def number_template(n):
    """ route that displays n if and only if n is a number
    """
    return render_template('./6-number_odd_or_even.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_even(n):
    """ route that displays n if and only if n is a number
    it also displays if the number is odd or even
    """
    return render_template('./6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """ Prevents execution when imported"""
    app.run(host='0.0.0.0', port=5000)
