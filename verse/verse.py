"""
This is the main app file in which all the blueprints are registered 
and attached to the flask aplication.
It also configures the database for apps usage and associates it with our app
as well as initialiazing the database 
Author:  Vincent M Karimi
"""

from flask import Flask
from resources import main_page, db, account, landing_page, shoper, agents
from waitress import serve #used when developing in windows environment as a server, it's serves the 
# equivalence of gunicorn in unix systems
import logging

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/verse_alx"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///verse.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
app.config["UPLOAD_PATH"] = "/uploads/"
db.init_app(app)

logging.basicConfig(level=logging.DEBUG)

app.register_blueprint(main_page)
app.register_blueprint(account)
app.register_blueprint(landing_page)
app.register_blueprint(shoper)
app.register_blueprint(agents)




with app.app_context():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    """
    This code will only be executed only if 
    this file is run as the main file and not being used in another file
    """
    app.debug = True
    app.run(host="0.0.0.0")
    #serve(app, host="0.0.0.0", port=5000)
    