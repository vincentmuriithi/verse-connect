from main import db, Product
from flask import Blueprint, url_for, render_template, request

admin = Blueprint("admin", __name__)

def add(product_name, description, product_size, product_image):
    product = Product(product_name=product_name, description=description, product_size=product_size, product_image=product_image)
    db.session.add(product)
    db.session.commit()

@admin.route("/admin")
def register():
    return "Admins page"
