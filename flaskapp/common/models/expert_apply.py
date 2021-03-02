# coding:utf-8
from application import db


class ExpertApply(db.Model):
    """

    """
    __tablename__ = "t_expert_apply"
    apply_id = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.BIGINT)

    username = db.Column(db.String(50))
    email = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    description = db.Column(db.String(100))
    realname = db.Column(db.String(50))
    job_title = db.Column(db.String(50))
    introduction = db.Column(db.String(100))

    create_time = db.Column(db.DATETIME)
    finish_time = db.Column(db.DATETIME)
    status = db.Column(db.CHAR, default=0)
