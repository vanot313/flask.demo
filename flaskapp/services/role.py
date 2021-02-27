from datetime import datetime
from common.models.role import role
from application import db


# 根据id搜索role
def getById(id):
    result = role.query.filter(role.id == int(id)).first()
    return result


# 根据 rolename 搜索role
def getByName(name):
    result = role.query.filter(role.rolename == name).first()
    return result


# 更新 role 信息
def update(entity):
    result = role.query.filter(role.id == entity.id).first()
    result = entity
    # result.modify_time = datetime.now()
    db.session.commit()
    return result


# 添加 role 信息
def add(entity):
    # entity.create_time = datetime.now()
    db.session.add(entity)
    db.session.commit()
    return entity


'''
# 删除 role 信息
def delete(id):
    result = role.query.filter(role.id == int(id)).first()
    result.status = '1'
    db.session.commit()
    return result
'''
