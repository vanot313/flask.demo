# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class work_order(db.Model):
    """
    用户表
    """
    __tablename__ = "t_work_order"
    order_id = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.BIGINT)
    file_name = db.Column(db.String(200))
    file_path = db.Column(db.String(200))
    method = db.Column(db.CHAR(1))
    expert_id = db.Column(db.BIGINT)
    expert_name = db.Column(db.String(50))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)
    status = db.Column(db.CHAR(1))

    # location = db.Column(db.String(128))
    # birth = db.Column(db.DATETIME)

    '''
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password
    '''
