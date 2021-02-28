from datetime import datetime
from common.models.work_order import WorkOrder
from application import db


# 根据user_id搜索 work_order
def getByUserId(id):
    result = WorkOrder.query.filter(WorkOrder.user_id == int(id)).filter(WorkOrder.status == 0).first()
    return result


# 根据order_id搜索 work_order
def getByOrderId(id):
    result = WorkOrder.query.filter(WorkOrder.order_id == int(id)).filter(WorkOrder.status == 0).first()
    return result


# 更新 work_order 信息
def update(entity):
    result = WorkOrder.query.filter(WorkOrder.user_id == entity.user_id).first()
    result = entity
    # result.modify_time = datetime.now()
    db.session.commit()
    return result


# 添加 work_order 信息
def add(entity):
    # entity.create_time = datetime.now()
    db.session.add(entity)
    db.session.commit()
    return entity


# 删除 work_order 信息
def delete(id):
    result = WorkOrder.query.filter(WorkOrder.user_id == int(id)).first()
    result.status = '1'
    db.session.commit()
    return result
