from datetime import datetime
from common.models.login_log import LoginLog
from application import db


class LoginLogDao:
    def getById(self, id):
        result = LoginLog.query.filter(LoginLog.id == int(id)).filter(LoginLog.status == 0)
        return result

    def getByName(self, name):
        result = LoginLog.query.filter(LoginLog.username == name)
        return result

    def getAll(self):
        result = LoginLog.query.all()
        return result

    def update(self, entity):
        result = LoginLog.query.filter(LoginLog.id == entity.id).first()
        result = entity
        result.modify_time = datetime.now()
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id):
        result = LoginLog.query.filter(LoginLog.id == int(id)).delete()
        db.session.commit()
        return result
