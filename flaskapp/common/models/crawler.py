# coding:utf-8
from application import db


class Crawler(db.Model):
    """

    """
    __tablename__ = "t_crawler"
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String(200))
    filepath = db.Column(db.String(200))
    datapath = db.Column(db.String(200))
    remarks = db.Column(db.String(200))
    status = db.Column(db.INT)
