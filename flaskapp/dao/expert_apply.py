from common.models.expert_apply import ExpertApply
from application import db


class ExpertApplyDao:
    def getByApplyId(self, id):
        result = ExpertApply.query.filter(ExpertApply.apply_id == int(id)).first()
        return result

    def getByUserId(self, id):
        result = ExpertApply.query.filter(ExpertApply.user_id == int(id)).first()
        return result

    def getByName(self, name):
        result = ExpertApply.query.filter(ExpertApply.username == name).first()
        return result

    def getAll(self):
        result = ExpertApply.query.all()
        return result

    def update(self, entity):
        result = ExpertApply.query.filter(ExpertApply.id == entity.id).first()
        result = entity
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
