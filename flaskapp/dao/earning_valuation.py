from common.models.earning_valuation import EarningValuation
from application import db


class EarningValuationDao:
    # 根据user_id搜索 work_order
    def getByUserId(self, id):
        result = EarningValuation.query.filter(EarningValuation.user_id == int(id))\
            .filter(EarningValuation.status == 0)
        return result

    # 根据order_id搜索 work_order
    def getByOrderId(self, id):
        result = EarningValuation.query.filter(EarningValuation.order_id == int(id))\
            .filter(EarningValuation.status == 0)
        return result

    def getAll(self):
        result = EarningValuation.query.all()
        return result

    # 更新 work_order 信息
    def update(self, entity):
        result = EarningValuation.query.filter(EarningValuation.order_id == entity.order_id).first()
        result = entity
        db.session.commit()
        return result

    # 添加 work_order 信息
    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

