# coding:utf-8
from application import db


class UserInfo(db.Model):
    """
    用户信息表
    """
    __tablename__ = "t_user_info"
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)
    last_login_time = db.Column(db.DATETIME)
    avator = db.Column(db.String(100), default="default")
    description = db.Column(db.String(100))
    msg_num = db.Column(db.INT, default=0)
    finished_num = db.Column(db.INT, default=0)
    waiting_num = db.Column(db.INT, default=0)
    data_assets = db.Column(db.FLOAT, default=0)

    birth = db.Column(db.DATE)
    location = db.Column(db.String(128))
    sex = db.Column(db.INT)

