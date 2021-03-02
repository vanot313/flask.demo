# coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class WorkOrder(db.Model):
    """
    工单表
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
    status = db.Column(db.CHAR(1), default=0)
    u_remarks = db.Column(db.String(500))
    e_remarks = db.Column(db.String(500))
    result = db.Column(db.FLOAT)

    # location = db.Column(db.String(128))
    # birth = db.Column(db.DATETIME)

    '''
        def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password
    '''
