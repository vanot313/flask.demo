# coding:utf-8
from application import db

class AdminInfo(db.Model):
    """

    """
    __tablename__ = "t_admin_info"
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)
    last_login_time = db.Column(db.DATETIME)
    avatar = db.Column(db.String(100))
    description = db.Column(db.String(100))

    location = db.Column(db.String(128))
    birth = db.Column(db.DATE)
