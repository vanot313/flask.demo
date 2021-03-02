from common.models.user_role import UserRole
from application import db


class UserRoleDao:
    def getById(self, id):
        result = UserRole.query.filter(UserRole.user_id == int(id)).filter(UserRole.status == 0)
        return result

    def getByName(self, name):
        result = UserRole.query.filter(UserRole.username == name)
        return result

    def update(self, entity):
        result = UserRole.query.filter(UserRole.user_id == entity.user_id).first()
        result = entity
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id, role):
        UserRole.query.filter(UserRole.id == int(id) and UserRole.role_id == int(role)).delete()
        db.session.commit()
        return []
