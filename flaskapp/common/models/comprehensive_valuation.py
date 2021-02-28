# coding:utf-8
from application import db


class ComprehensiveValuation(db.Model):
    """

    """
    __tablename__ = "t_comprehensive_valuation"
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT)
    full = db.Column(db.FLOAT)
    correct = db.Column(db.FLOAT)
    uniformity = db.Column(db.FLOAT)
    repeatability = db.Column(db.FLOAT)
    rareness = db.Column(db.FLOAT)
    timeliness = db.Column(db.FLOAT)
    dimensional = db.Column(db.FLOAT)
    economy = db.Column(db.FLOAT)
    quality_weight = (db.Column(db.TEXT))
    applied_weight = (db.Column(db.TEXT))
    RI = (db.Column(db.TEXT))
    Sq = db.Column(db.String(50))
    Sa = db.Column(db.String(50))
    S = db.Column(db.String(50))