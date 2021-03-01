from common.models.expert_info import ExpertInfo
from application import db


class ExpertInfoDao:
    def getById(self, id):
        result = ExpertInfo.query.filter(ExpertInfo.id == int(id)).first()
        return result

    def getByName(self, name):
        result = ExpertInfo.query.filter(ExpertInfo.username == name).first()
        return result

    def update(self, entity):
        result = ExpertInfo.query.filter(ExpertInfo.id == entity.id).first()
        result = entity
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
