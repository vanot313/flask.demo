from common.models.admin_info import AdminInfo
from application import db


class AdminInfoDao:
    def getById(self, id):
        result = AdminInfo.query.filter(AdminInfo.id == int(id))
        return result

    def getByName(self, name):
        result = AdminInfo.query.filter(AdminInfo.username == name)
        return result

    def getAll(self):
        result = AdminInfo.query.all()
        return result

    def update(self, entity):
        result = AdminInfo.query.filter(AdminInfo.id == entity.id).first()
        result = entity
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    # 保留
    def delete(self, id):
        AdminInfo.query.filter(AdminInfo.id == int(id)).delete()
        db.session.commit()
        return []
