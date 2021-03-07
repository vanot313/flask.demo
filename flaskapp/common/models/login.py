# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class Login(db.Model):
    """

    """
    __tablename__ = "v_login"
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    _password_ = db.Column(db.String(128))
    status = db.Column(db.CHAR(1))
    rolename = db.Column(db.String(100), primary_key=True)

    @property
    def password(self):
        raise Exception('密码不能被读取')

    # 赋值password，则自动加密存储。
    @password.setter
    def password(self, value):
        self.password = generate_password_hash(value)

    # 使用check_password,进行密码校验，返回True False。
    def check_password(self, pasword):
        return check_password_hash(self._password_, pasword)