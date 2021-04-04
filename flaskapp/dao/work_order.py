from datetime import datetime

from sqlalchemy import *

from common.models.work_order import WorkOrder
from application import db


class WorkOrderDao:
    # 根据user_id搜索 work_order
    def getByUserId(self, id, status=None):
        result = WorkOrder.query.filter(WorkOrder.user_id == int(id))

        if status is not None:
            result.filter(WorkOrder.status == status)

        return result

    # 根据order_id搜索 work_order
    def getByOrderId(self, id, status=None):
        result = WorkOrder.query.filter(WorkOrder.order_id == id)

        # if status is not None:
        #     result.filter(WorkOrder.status == status)

        return result

    def getAll(self, status=None):
        result = WorkOrder.query.all()

        if status is not None:
            result.filter(WorkOrder.status == status)

        return result

    def getFuzzy(self, user_id="", order_id="", expert_id="", status="", page="1", per_page="10"):
        if page is None:
            page = 1
        if per_page is None:
            per_page = 10
        if order_id is None:
            order_id = ''

        key1 = or_(WorkOrder.user_id.like("%" + str(user_id) + "%"), WorkOrder.user_id.is_(None))
        key2 = or_(WorkOrder.order_id.like("%" + str(order_id) + "%"), WorkOrder.order_id.is_(None))
        key3 = or_(WorkOrder.expert_id.like("%" + str(expert_id) + "%"), WorkOrder.expert_id.is_(None))
        key4 = or_(WorkOrder.status.like("%" + str(status) + "%"), WorkOrder.status.is_(None))

        if user_id is not "":
            key1 = WorkOrder.user_id.like("%" + str(user_id) + "%")
        if order_id is not "":
            key2 = WorkOrder.order_id.like("%" + str(order_id) + "%")
        if expert_id is not "":
            key3 = WorkOrder.expert_id.like("%" + str(expert_id) + "%")
        if status is not "":
            key4 = WorkOrder.status.like("%" + str(status) + "%")

        result = WorkOrder.query.order_by(WorkOrder.modify_time.desc()).filter(
            and_(
                key1,
                key2,
                key3,
                key4
            )
        )

        result = result.paginate(page=int(page), per_page=int(per_page))
        ans = {}
        ans['data'] = result.items
        ans['pages'] = result.pages
        ans['total'] = result.total

        return ans

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
