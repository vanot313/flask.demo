from datetime import datetime
from common.models.user import User
from application import db


# 根据id搜索user
def getById(id):
    result = User.query.filter(User.user_id == int(id)).filter(User.status == 0).first()
    return result


# 根据id搜索user
def getByName(name):
    result = User.query.filter(User.username == name).first()
    return result


# 更新user信息
def update(entity):
    result = User.query.filter(User.user_id == entity.user_id).first()
    result = entity
    result.modify_time = datetime.now()
    db.session.commit()
    return result


# 添加user信息
def add(entity):
    # entity.create_time = datetime.now()
    db.session.add(entity)
    db.session.commit()
    return entity


# 删除 user 信息
def delete(id):
    result = User.query.filter(User.user_id == int(id)).first()
    result.status = '1'
    db.session.commit()
    return result
