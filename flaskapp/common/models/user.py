# coding:utf-8
from application import db


class User(db.Model):
    """
    用户表
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
