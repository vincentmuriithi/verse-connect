from flask import render_template, redirect, request, Blueprint, current_app, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from mongoengine import NotUniqueError
import bcrypt
from .verse_mongodb import agent, disconnect, verse_connect

agents = Blueprint("agents", __name__)

@agents.route("/uploads/<filename>")
def retrieve(filename):
    print(filename)
    my_path = os.path.dirname(os.path.abspath(__file__))
    print(my_path)
    uploads_path = os.path.join(my_path, "..", "uploads/images")
    print(uploads_path)
    return send_from_directory(uploads_path, filename)


@agents.route("/verse_dashboard/<name>/<email>", methods = ["GET", "POST"])
def dashboard(name, email):
    if not name:
        return redirect(url_for("agents.login"))
    verse_connect()
    agent1 = agent.objects(email=email).first()
    details = {
        "name" : agent1.name,
        "email" : agent1.email,
        "location" : agent1.location,
        "tel" : agent1.tel
        }
    file_url = url_for("agents.retrieve", filename="beauty.jpg")
    print(file_url)
    disconnect()
    return render_template("agent_dashboard.html", file_url=file_url, details=details)

abs_path = os.path.dirname(os.path.abspath(__file__))
new_path = os.path.join(abs_path, "..")

@agents.route("/verse_uploads", methods = ["POST"])
def upload():
    if request.method == "POST":
        if 'profile_pic' in request.files:
            uploaded_file = request.files['profile_pic']
            if uploaded_file.filename != '':
                print("file uploaded")
                filename = secure_filename(uploaded_file.filename)
                file_path = os.path.join(new_path, 'uploads/images/')
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                    print(f"{file_path} created")
                upload_path = os.path.join(file_path, filename)
                try:
                    uploaded_file.save(upload_path)
                    print(f"file has been uploaded and saved to {upload_path}")
                except Exception as e:
                    print(f"{e}")
    return redirect(url_for('agents.dashboard'))

@agents.route("/verse_signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        location = request.form.get("location")
        password = request.form.get("password")
        tel = request.form.get("tel")
        if name and email and password and location:
            password = password.encode("utf-8")
            password = bcrypt.hashpw(password, bcrypt.gensalt())
            details = {
                "name" : name,
                "password" : password,
                "email": email,
                "location" : location,
                "tel" : tel
                }
            try:
                verse_connect()
                agent1 = agent(**details)
                if agent1.save():
                    disconnect()
                    return redirect(url_for("agents.dashboard", name=name, email=email))
            except NotUniqueError as e:
                print(e)
    return render_template("verse-signup.html")

@agents.route("/verse_login", methods=["GET", "POST"])
def login():
    return render_template("verse-login.html")