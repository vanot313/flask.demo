from common.models.user_info import UserInfo
from application import db


class UserInfoDao:
    def getById(self, id):
        result = UserInfo.query.filter(UserInfo.id == int(id))
        return result

    def getByName(self, name):
        result = UserInfo.query.filter(UserInfo.username == name)
        return result

    def getAll(self):
        result = UserInfo.query.all()
        return result

    def update(self, entity):
        result = UserInfo.query.filter(UserInfo.id == entity.id).first()
        result = entity
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    # 保留
    def delete(self, id):
        UserInfo.query.filter(UserInfo.id == int(id)).delete()
        db.session.commit()
        return []