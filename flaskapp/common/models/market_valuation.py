# coding:utf-8
from application import db


class MarketValuation(db.Model):
    """

    """
    __tablename__ = "t_market_valuation"
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT)
    graininess = db.Column(db.INT)
    dimension = db.Column(db.INT)
    activity = db.Column(db.INT)
    scale = db.Column(db.INT)
    correlation = db.Column(db.INT)
    suggestion = db.Column(db.BIGINT)

    amount = db.Column(db.FLOAT)
    size = db.Column(db.FLOAT)
    growth = db.Column(db.FLOAT)
    coverage = db.Column(db.FLOAT)
    attribute = db.Column(db.FLOAT)
    source = db.Column(db.FLOAT)
    maintenance = db.Column(db.FLOAT)
    incoming = db.Column(db.FLOAT)
    outgoing = db.Column(db.FLOAT)
