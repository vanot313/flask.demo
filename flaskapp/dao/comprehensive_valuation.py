from common.models.comprehensive_valuation import ComprehensiveValuation
from application import db


class ComprehensiveValuationDao:
    # 根据user_id搜索 work_order
    def getByUserId(self, id):
        result = ComprehensiveValuation.query.filter(ComprehensiveValuation.user_id == int(id))
        return result

    # 根据order_id搜索 work_order
    def getByOrderId(self, id):
        result = ComprehensiveValuation.query.filter(ComprehensiveValuation.order_id == int(id))
        return result

    def getAll(self):
        result = ComprehensiveValuation.query.all()
        return result

    # 更新 work_order 信息
    def update(self, entity):
        result = ComprehensiveValuation.query.filter(ComprehensiveValuation.order_id == entity.order_id).first()
        result = entity
        db.session.commit()
        return result

    # 添加 work_order 信息
    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

