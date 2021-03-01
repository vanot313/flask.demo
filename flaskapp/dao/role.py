from datetime import datetime
from common.models.role import Role
from application import db


class RoleDao:
    # 根据id搜索role
    def getById(self, id):
        result = Role.query.filter(Role.id == int(id)).first()
        return result

    # 根据 rolename 搜索role
    def getByRolename(self, name):
        result = Role.query.filter(Role.rolename == name).first()
        return result

    # 更新 role 信息
    def update(self, entity):
        result = Role.query.filter(Role.id == entity.id).first()
        result = entity
        db.session.commit()
        return result

    # 添加 role 信息
    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

