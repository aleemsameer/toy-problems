import os
import datetime
from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
s = db()

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        timestamp = datetime.datetime.now()
        print("Name:", name)
        print("Email:", email)
        user = User(name = name, email = email, password = password, timestamp = timestamp)
        try:
            s.add(user)
            s.commit()
            return render_template("hello.html", name = name)
        except:
            return render_template("error.html")
    return render_template("register.html")
@app.route("/admin", methods = ["GET"])
def admin():
    data = db.query(User)
    return render_template("admin.html", users = data)