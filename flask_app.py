from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

app.config['SECRET_KEY']="my secret key here"


