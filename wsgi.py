# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, render_template
from game import Game

app = Flask(__name__)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)