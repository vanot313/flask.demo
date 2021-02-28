from common.models.user_info import User_info
from application import db


# 根据id搜索User_info
def getById(id):
    result = User_info.query.filter(User_info.user_id == int(id)).first()
    return result


# 根据id搜索User_info
def getByName(name):
    result = User_info.query.filter(User_info.username == name).first()
    return result


# 更新User_info信息
def update(entity):
    result = User_info.query.filter(User_info.user_id == entity.user_id).first()
    result = entity
    # result.modify_time = datetime.now()
    db.session.commit()
    return result


# 添加User_info信息
def add(entity):
    # entity.create_time = datetime.now()
    db.session.add(entity)
    db.session.commit()
    return entity
