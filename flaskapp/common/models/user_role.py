# coding:utf-8
from application import db


class UserRole(db.Model):
    """
    用户表
    """
    __tablename__ = "t_user_role"
    user_id = db.Column(db.BIGINT, primary_key=True)
    role_id = db.Column(db.BIGINT, primary_key=True)

    '''
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password
    '''
