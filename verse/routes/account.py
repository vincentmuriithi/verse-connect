from flask import Blueprint, render_template, request
from .verse_tables import db, Client, Order
"""
This module contains the customers account implementation 
code to serve the /account url path page
Author:  Vincent M Karimi
"""

account = Blueprint("account", __name__)

@account.route("/account")
def show():
    client1 = Client(name="Vincent")
    client2 = Client(name="Karimi")
    db.session.add_all([client1, client2])
    db.session.commit()
    print(client1.id)
    order1 = Order(client_id=client1.id, product="Short dress")
    order2 = Order(client_id=client2.id, product="long dress")
    order3 = Order(client_id=client1.id, product="red dress")
    db.session.add_all([order1, order2, order3])
    db.session.commit()
    req = db.session.query(Order).all()
    return render_template("acc.html", req=req)
