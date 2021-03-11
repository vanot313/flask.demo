# coding:utf-8
from application import db


class ExpertInfo(db.Model):
    """

    """
    __tablename__ = "t_expert_info"
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)
    last_login_time = db.Column(db.DATETIME)
    avatar = db.Column(db.String(100))
    description = db.Column(db.String(100))
    realname = db.Column(db.String(50))
    job_title = db.Column(db.String(50))
    introduction = db.Column(db.String(100))
    finished_num = db.Column(db.INT, default=0)
    waiting_num = db.Column(db.INT, default=0)
    score = db.Column(db.FLOAT, default=0)

    location = db.Column(db.String(128))
    birth = db.Column(db.DATE)
