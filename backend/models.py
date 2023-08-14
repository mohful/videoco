import email
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    date_of_delivery = db.Column(db.Date)
    date_of_return = db.Column(db.Date)
    status_of_order = db.Column(db.String(255))

    def __repr__(self):
        return '%r' % self.order_id

    def to_dict(self):
        return {"order_id": self.order_id, "customer_id": self.customer_id, "date_of_order": self.date_of_order, "date_of_delivery": self.date_of_delivery, "date_of_return": self.date_of_return}

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    card_number = db.Column(db.Integer)
    shipping_address = db.Column(db.String(255))
    billing_address = db.Column(db.String(255))
    loyalty_balance = db.Column(db.Integer)
    free_movies = db.Column(db.Integer)

    def __repr__(self):
        return '%s' % self.id

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "phone": self.phone, "card_number": self.card_number, "shipping_address": self.shipping_address, 
        "billing_address": self.billing_address, "loyalty_balance": self.loyalty_balance, "free_movies": self.free_movies}

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    date_of_release = db.Column(db.Date)
    movie_count = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __repr__(self):
        return '%r' % self.id
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description, "date_of_release": self.date_of_release, "movie_count": self.movie_count, "price": self.price}


class Persons(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    type = db.Column(db.String(10))

    def __repr__(self):
        return '%r' % self.id

    def to_dict(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "type": self.type}

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    hire_date = db.Column(db.Date)
    location = db.Column(db.String(100))
    contact_number = db.Column(db.Integer)
    employee_type = db.Column(db.Integer)

    def __repr__(self):
        return '%r' % self.id

    def to_dict(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email, "hire_date": self.hire_date, "location": self.location, "contact_number": self.contact_number, "employee_type": self.employee_type}


class GeneralCategory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_type = db.Column(db.String(100))
    category_name = db.Column(db.String(100))

    def __repr__(self):
        return '%r' % self.id

    def to_dict(self):
        return {"id": self.id, "category_type": self.category_type, "category_name": self.category_name}


class MovieDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    person_id = db.Column(db.Integer, db.ForeignKey("actors.id"))

    def __repr__(self):
        return '%r' % self.id

    def to_dict(self):
        return {"id": self.id, "movie_id": self.movie_id, "person_id": self.person_id}