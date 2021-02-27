# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class User(db.Model):
    """
    用户表
    """
    __tablename__ = "t_user"
    user_id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(128))
    status = db.Column(db.CHAR(1))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)

    # location = db.Column(db.String(128))
    # birth = db.Column(db.DATETIME)

    @property
    def password(self):
        raise Exception('密码不能被读取')

    # 赋值password，则自动加密存储。
    @password.setter
    def password(self, value):
        self.password = generate_password_hash(value)

    # 使用check_password,进行密码校验，返回True False。
    def check_password(self, pasword):
        return check_password_hash(self.password, pasword)

    '''
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password
    '''
