from common.models.user_role import User_role
from application import db


# 根据id搜索 User_role
def getById(id):
    result = User_role.query.filter(User_role.user_id == int(id)).filter(User_role.status == 0).first()
    return result


# 根据id搜索 User_role
def getByName(name):
    result = User_role.query.filter(User_role.username == name).first()
    return result


# 更新 User_role 信息
def update(entity):
    result = User_role.query.filter(User_role.user_id == entity.user_id).first()
    result = entity
    db.session.commit()
    return result


# 添加 User_role 信息
def add(entity):
    # entity.create_time = datetime.now()
    db.session.add(entity)
    db.session.commit()
    return entity
