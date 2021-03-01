# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class Role(db.Model):
    """
    用户表
    """
    __tablename__ = "t_role"
    id = db.Column(db.BIGINT, primary_key=True)
    rolename = db.Column(db.String(100))
    remark = db.Column(db.String(100))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)

    # status = db.Column(db.CHAR(1))

    '''
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password
    '''
