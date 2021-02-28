# coding:utf-8
from application import db


class CostValuation(db.Model):
    """

    """
    __tablename__ = "t_cost_valuation"
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT)
    P = db.Column(db.FLOAT)
    R = db.Column(db.FLOAT)
    C = db.Column(db.FLOAT)
    II = db.Column(db.FLOAT)
    M = db.Column(db.FLOAT)
    E = db.Column(db.FLOAT)
