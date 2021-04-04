# coding:utf-8
from application import db


class MarketValuation(db.Model):
    """

    """
    __tablename__ = "t_market_valuation"
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT)
    graininess = db.Column(db.FLOAT)
    dimension = db.Column(db.FLOAT)
    activity = db.Column(db.FLOAT)
    scale = db.Column(db.FLOAT)
    correlation = db.Column(db.FLOAT)
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
