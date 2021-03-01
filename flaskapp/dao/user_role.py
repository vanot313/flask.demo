from common.models.user_role import UserRole
from application import db


class UserRoleDao:
    # 根据id搜索 User_role
    def getById(self, id):
        result = UserRole.query.filter(UserRole.user_id == int(id)).filter(UserRole.status == 0)
        return result

    # 根据id搜索 User_role
    def getByName(self, name):
        result = UserRole.query.filter(UserRole.username == name)
        return result

    # 弃用 权限表只有增加和删除操作
    def update(self, entity):
        result = UserRole.query.filter(UserRole.user_id == entity.user_id).first()
        result = entity
        db.session.commit()
        return result

    # 添加 User_role 信息
    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
