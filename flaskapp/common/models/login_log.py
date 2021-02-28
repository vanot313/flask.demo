# coding:utf-8
from application import db


class LoginLog(db.Model):
    """

    """
    __tablename__ = "t_login_log"
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    login_time = db.Column(db.TIMESTAMP)
    rolename = db.Column(db.String(100))
    location = db.Column(db.String(50))
    ip = db.Column(db.String(50))
    login_system = db.Column(db.String(50))
    browser = db.Column(db.String(50))
