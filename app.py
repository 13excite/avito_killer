from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_args
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


def get_items_per_page(items_result, offset=0, per_page=10):
    """
    :param items_result: result of select db
    :param offset: from 0 by default
    :param per_page: show item on page, default = 10
    :return: slice of select result
    """
    return items_result[offset: offset + per_page]


@app.route("/items/<breed>/", methods=['GET'])
def index_list(breed):
    errors = []
    try:
        result = Item.query.filter_by(translate_breed=breed).all()
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')

        items = get_items_per_page(result, offset=offset, per_page=per_page)
        total = len(result)

        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('item.html',
                               items=items,
                               page=page,
                               per_page=per_page,
                               pagination=pagination,
                               )
    except Exception as err:
        print(err)
        errors.append("Couldn't get results.")
        return render_template('error.html', errors=errors)


if __name__ == '__main__':
    app.run()
