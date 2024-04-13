"""
This specific module serves as the main entry of the flask app
and it contain's the code implementation that serves and renders the 
main route of the verse app
Author:  Vincent M Karimi
"""

from contextlib import nullcontext
from sqlite3 import IntegrityError
from flask import Blueprint, render_template, request, url_for
from sqlalchemy.exc import IntegrityError
main_page = Blueprint("main_page", __name__)
from datetime import datetime
from .verse_tables import db

class Product(db.Model):
    id = db.Column("product_id", db.Integer, primary_key=True)
    product_name = db.Column(db.String(60))
    description = db.Column(db.Text)
    product_size = db.Column(db.Integer)
    product_image = db.Column(db.String(160), unique=True, nullable=False)
    product_price = db.Column(db.Integer)
    date_time = db.Column(db.Date, default=datetime.utcnow)

def add(product_name, description, product_size, product_image, product_price):
    product = Product(product_name=product_name, 
                      description=description, 
                      product_size=product_size, 
                      product_image=product_image,
                      product_price=product_price)
    db.session.add(product)
    db.session.commit()
image_array = [
        "images/dress1.jpg",
        "images/dress2.jpg",
        "images/dress3.jpg",
        "images/dress4.jpg",
        "images/dress5.jpg"
    ];
@main_page.route("/")
def main():
    name = "Happy shopping"
    items = db.session.query(Product).all()
    try:
        for k in image_array:
            add("dress", "available in various colors", 4, k, 250)
        return render_template("main.html", name=name, items=items)
    except IntegrityError:
        db.session.rollback()
        return render_template("main.html", name=name, items=items)
