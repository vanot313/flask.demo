# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class User_info(db.Model):
    """
    用户表
    """
    __tablename__ = "t_user_info"
    user_id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)
    last_login_time = db.Column(db.DATETIME)
    avatar = db.Column(db.String(100))
    description = db.Column(db.String(100))
    msg_num = db.Column(db.INT)
    finished_num = db.Column(db.INT)
    waiting_num = db.Column(db.INT)
    data_assets = db.Column(db.FLOAT)

    # location = db.Column(db.String(128))
    # birth = db.Column(db.DATETIME)

    '''
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password
    '''
