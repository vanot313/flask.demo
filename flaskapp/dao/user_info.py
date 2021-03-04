from sqlalchemy import *

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

    def getFuzzy(self, id, username, email, location):

        key1 = or_(UserInfo.username.like("%" + username + "%"), UserInfo.username.is_(None))
        key2 = or_(UserInfo.id.like("%" + id + "%"), UserInfo.id.is_(None))
        key3 = or_(UserInfo.email.like("%" + email + "%"), UserInfo.email.is_(None))
        key4 = or_(UserInfo.location.like("%" + location + "%"), UserInfo.location.is_(None))

        if username is not "":
            key1 = UserInfo.username.like("%" + username + "%")
        if id is not "":
            key2 = UserInfo.id.like("%" + id + "%")
        if email is not "":
            key3 = UserInfo.email.like("%" + email + "%")
        if location is not "":
            key4 = UserInfo.location.like("%" + location + "%")

        result = UserInfo.query.filter(
            and_(
                key1,
                key2,
                key3,
                key4)
        )

        return result
