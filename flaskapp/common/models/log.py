# coding:utf-8
from application import db


class Log(db.Model):
    """

    """
    __tablename__ = "t_log"
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    operation = db.Column(db.TEXT)
    time = db.Column(db.DECIMAL)
    method = db.Column(db.TEXT)
    params = db.Column(db.TEXT)
    ip = db.Column(db.String(64))
    create_time = db.Column(db.TIMESTAMP)
    location = db.Column(db.String(50))
    from_id = db.Column(db.BIGINT)
    to_id = db.Column(db.BIGINT)
    order_id = db.Column(db.BIGINT)
