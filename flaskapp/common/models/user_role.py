# coding:utf-8
from application import db


class User_role(db.Model):
    """
    用户表
    """
    __tablename__ = "t_user_role"
    user_id = db.Column(db.BIGINT)
    role_id = db.Column(db.BIGINT)

    '''
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password
    '''
