#!/usr/bin/python3
""" A simple Flask app """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display "HBNB" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_root(text):
    """making a dynamic URL by taking a variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>/", strict_slashes=False)
def python(text="is cool"):
    """displays python + text """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>",  strict_slashes=False)
def number(n):
    """displays n is anulber if int is 1"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
