from datetime import datetime
from common.models.log import Log
from application import db


class LogDao:
    def getById(self, id):
        result = Log.query.filter(Log.id == int(id)).filter(Log.status == 0).first()
        return result

    def getByName(self, name):
        result = Log.query.filter(Log.username == name)
        return result

    def update(self, entity):
        result = Log.query.filter(Log.id == entity.id).first()
        result = entity
        result.modify_time = datetime.now()
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id):
        result = Log.query.filter(Log.id == int(id)).delete()
        db.session.commit()
        return result
