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
    breed_disct = {}
    errors = []
    try:
        for b in Item.query.with_entities(Item.breed, Item.translate_breed).distinct().order_by(Item.breed):
            breed_disct[b.breed] = b.translate_breed
    except Exception:
        errors.append("Couldn't connect to database.")
    return render_template('index.html', breeds=breed_disct, errors=errors)


@app.route("/items/<breed>/", methods=['GET'])
def index_list(breed):
    items_dict = {}
    errors = []
    try:
        page = int(request.args.get('p'))
    except:
        page = 1
    try:
        for q in Item.query.filter_by(translate_breed=breed).all():
            items_dict[q.id] = {'title': q.title}
            items_dict[q.id].update({'price': q.price})
            items_dict[q.id].update({'breed': q.breed})
            items_dict[q.id].update({'address': q.address})
            items_dict[q.id].update({'desc': q.description})
            items_dict[q.id].update({'date': q.start_date})
    except Exception as err:
        print(err)
        errors.append("Couldn't connect to database.")
    return render_template('item.html', ad_dicts=items_dict, errors=errors)


if __name__ == '__main__':
    app.run()
