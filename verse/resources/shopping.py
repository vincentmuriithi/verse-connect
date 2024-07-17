from flask import Blueprint, url_for, render_template, request
from .main import db
from .mystore import *


shoper = Blueprint("shopping", __name__)
items = [shoes, dresses, clothes, sneakers, bags]

@shoper.route("/shopping")
def shop():
    return render_template("shopping.html", shoes=shoes, items=items)

@shoper.route("/payment")
def pay():
    return render_template("verse_pay.html") 

@shoper.route("/product/<path:product_name>")
def view(product_name):
    return render_template("product.html", prod=product_name)