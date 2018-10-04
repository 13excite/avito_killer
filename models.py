from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    items = db.relationship('Item', backref='user_info')

    def __init__(self, login, email):
        self.login = login
        self.email = email

    def __repr__(self):
        return '<Uid {}>'.format(self.user_id)


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    start_date = db.Column(db.DateTime, default=db.func.now())
    img_url = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=True)
    address = db.Column(db.String(50))
    description = db.Column(db.String(255))
    breed = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, start_date, img_url, price, address, description, breed, user_id):
        self.title = title
        self.start_date = start_date
        self.img_url = img_url
        self.price = price
        self.address = address
        self.description = description
        self.breed = breed
        self.user_id = user_id

    def __repr__(self):
        return '<Iid {}>'.format(self.item_id)
