from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    _tablename_ = "Users"
    username =db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    timestamp=db.Column(db.String, nullable=False)

class BOOKS(db.Model):
    __tablename__ = "BOOKS"
    isbn =db.Column(db.String, primary_key=True)
    tittle = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)



    