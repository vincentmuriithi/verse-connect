"""
This module is a bluprint that contains the code implementation
that serves the landingpage route path url
Author:  Vincent M Karimi
"""

#importing the necessary modules
from flask import Blueprint, render_template, url_for, redirect

#Registering the landing_page blueprint
landing_page = Blueprint("landing_page", __name__)


@landing_page.route("/about")
def land():
    return render_template("about.html")

@landing_page.route("/redirect_verse")
def verse_redirect():
    return redirect(url_for("main_page.main"))
