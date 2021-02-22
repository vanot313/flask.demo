# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class admin(db.Model):
    __tablename__ = 't_admin'

    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    _password_ = db.Column(db.String(128))
    email = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    status = db.Column(db.CHAR(1))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)
    last_login_time = db.Column(db.DATETIME)
    avatar = db.Column(db.String(100))
    description = db.Column(db.String(100))

    @property
    def password(self):
        raise Exception('密码不能被读取')

    # 赋值password，则自动加密存储。
    @password.setter
    def password(self, value):
        self._password_ = generate_password_hash(value)

    # 使用check_password,进行密码校验，返回True False。
    def check_password(self, pasword):
        return check_password_hash(self._password_, pasword)

