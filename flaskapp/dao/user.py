from datetime import datetime
from common.models.user import User
from application import db


class UserDao:
    # 根据id搜索user
    def getById(self, id):
        result = User.query.filter(User.id == int(id)).filter(User.status == 0)
        return result

    def getByName(self, name):
        result = User.query.filter(User.username == name)
        return result

    def getAll(self):
        result = User.query.all()
        return result

    # 更新user信息
    def update(self, entity):
        result = User.query.filter(User.id == entity.id).first()
        result = entity
        result.modify_time = datetime.now()
        db.session.commit()
        return result

    # 添加user信息
    def add(self, entity):
        # entity.create_time = datetime.now()
        db.session.add(entity)
        db.session.commit()
        return entity

    # 冻结 user 信息
    def freeze(self, id):
        result = User.query.filter(User.id == int(id)).first()
        result.status = '1'
        db.session.commit()
        return result

    # 删除 user 信息
    def delete(self, id):
        User.query.filter(User.id == int(id)).delete()
        db.session.commit()
        return []