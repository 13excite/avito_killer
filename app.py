from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Item


@app.route('/')
def main_index():
    breed_list = []
    for b in Item.query.with_entities(Item.breed).distinct().order_by(Item.breed):
        breed_list.append(b.breed)
    return render_template('index.html', breeds=breed_list)


@app.route("/items/<number>", methods=['GET'])
def hello_name(number):
    return "Hello {}!".format(number)


if __name__ == '__main__':
    app.run()
