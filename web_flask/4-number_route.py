#!/usr/bin/python3
"""
Starts a Flask web application

must be listening on 0.0.0.0, port 5000

Routes:
/: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C ", followed by the value of the text
variable (replace underscore _ symbols with a space )

/python/(<text>): display "Python ", followed by the value of the text
 variable (replace underscore _ symbols with a space )
The default value of text is "is cool"
/number/<n>: display "n is a number" only if n is an integer

"""

from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display C is ..."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Display python is..."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int n>', strict_slashes=False)
def number(n):
    """Display n is a number"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')