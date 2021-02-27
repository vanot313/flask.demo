from datetime import datetime
from common.models.work_order import work_order
from application import db


# 根据user_id搜索 work_order
def getByUserId(id):
    result = work_order.query.filter(work_order.user_id == int(id)).filter(work_order.status == 0).first()
    return result


# 根据order_id搜索 work_order
def getByOrderId(id):
    result = work_order.query.filter(work_order.order_id == int(id)).filter(work_order.status == 0).first()
    return result


# 更新 work_order 信息
def update(entity):
    result = work_order.query.filter(work_order.user_id == entity.user_id).first()
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
    result = work_order.query.filter(work_order.user_id == int(id)).first()
    result.status = '1'
    db.session.commit()
    return result
