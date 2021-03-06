from common.models import *
from application import db


class CostValuationDao:
    # 根据user_id搜索 work_order
    def getByUserId(self, id):
        result = CostValuation.query.filter(CostValuation.user_id == int(id))\
            .filter(CostValuation.status == 0)
        return result

    # 根据order_id搜索 work_order
    def getByOrderId(self, id):
        result = CostValuation.query.filter(CostValuation.order_id == int(id))
        return result

    def getAll(self):
        result = CostValuation.query.all()
        return result

    # 更新 work_order 信息
    def update(self, entity):
        result = CostValuation.query.filter(CostValuation.order_id == entity.order_id).first()
        result = entity
        db.session.commit()
        return result

    # 添加 work_order 信息
    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
