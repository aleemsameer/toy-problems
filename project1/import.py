import os, csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
def main():
    db.create_all()
    with open("books.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for r in reader:
            thisBook = Book(r[0], r[1], r[2], int(r[3]))
            db.session.add(thisBook)
    db.session.commit()
    print("Uploaded book data into book data base")

if __name__ == "_main_":
  with app.app_context():
      main()