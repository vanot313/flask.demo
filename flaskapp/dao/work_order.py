from datetime import datetime

from sqlalchemy import *

from common.models.work_order import WorkOrder
from application import db


class WorkOrderDao:
    # 根据user_id搜索 work_order
    def getByUserId(self, id):
        result = WorkOrder.query.filter(WorkOrder.user_id == int(id))\
            .filter(WorkOrder.status == 0)
        return result

    # 根据order_id搜索 work_order
    def getByOrderId(self, id):
        result = WorkOrder.query.filter(WorkOrder.order_id == int(id))\
            .filter(WorkOrder.status == 0)
        return result

    def getAll(self):
        result = WorkOrder.query.all()
        return result

    # 更新 work_order 信息
    def update(self, entity):
        result = WorkOrder.query.filter(WorkOrder.order_id == entity.order_id).first()
        result = entity
        db.session.commit()
        return result

    # 添加 work_order 信息
    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    # 冻结 work_order 信息
    def freeze(self, id):
        result = WorkOrder.query.filter(WorkOrder.order_id == int(id)).first()
        result.status = '1'
        db.session.commit()
        return result

    # 删除 work_order 信息
    def delete(self, id):
        WorkOrder.query.filter(WorkOrder.order_id == int(id)).delete()
        db.session.commit()
        return []

    def getFuzzy(self, order_id):

        key1 = or_(WorkOrder.order_id.like("%" + order_id + "%"), WorkOrder.order_id.is_(None))
        # key2 = or_(UserInfo.id.like("%" + id + "%"), UserInfo.id.is_(None))
        # key3 = or_(UserInfo.email.like("%" + email + "%"), UserInfo.email.is_(None))
        # key4 = or_(UserInfo.location.like("%" + location + "%"), UserInfo.location.is_(None))

        if order_id is not "":
            key1 = WorkOrder.order_id.like("%" + order_id + "%")
        # if id is not "":
        #     key2 = UserInfo.id.like("%" + id + "%")
        # if email is not "":
        #     key3 = UserInfo.email.like("%" + email + "%")
        # if location is not "":
        #     key4 = UserInfo.location.like("%" + location + "%")

        result = WorkOrder.query.filter(
            and_(
                key1,
                # key2,
                # key3,
                # key4
            )
        )

        return result