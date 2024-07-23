from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    order = db.relationship("Order", backref="clients", cascade="all, delete-orphan")

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer,db.ForeignKey("client.id", ondelete="CASCADE"), nullable=False)
    product = db.Column(db.String(60),nullable=False)

