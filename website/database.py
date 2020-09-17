from website import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    pwd = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, pwd, email):
        super().__init__()
        self.pwd = pwd
        self.name = name
        self.email = email