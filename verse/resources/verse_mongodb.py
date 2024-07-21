from pymongo import MongoClient
from mongoengine import *

def verse_connect():
    connect(db="verse-connect", host="localhost", port=27017)

class agent(Document):
    name = StringField(max_length=20)
    email = EmailField(required=True, unique=True)
    product_sub = DictField()
    service_sub = DictField()
    profile_pic = BinaryField()
    location = StringField(max_length=20)
    password = StringField(max_length=150)
    tel = IntField()





