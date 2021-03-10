# coding:utf-8
from application import db


class EarningValuation(db.Model):
    """

    """
    __tablename__ = "t_earning_valuation"
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT)
    P = db.Column(db.FLOAT)
    n = db.Column(db.FLOAT)
    r = db.Column(db.FLOAT)
    RI = (db.Column(db.TEXT))
