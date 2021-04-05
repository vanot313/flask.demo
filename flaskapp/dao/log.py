from datetime import datetime

from sqlalchemy import *

from common.models.log import Log
from application import db


class LogDao:
    def getById(self, id):
        result = Log.query.filter(Log.id == int(id)).filter(Log.status == 0)
        return result

    def getByName(self, name):
        result = Log.query.filter(Log.username == name)
        return result

    def getAll(self):
        result = Log.query.all()
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
        Log.query.filter(Log.id == int(id)).delete()
        db.session.commit()
        return []

    def getByUser(self, user_id, page="1", per_page="10"):
        if page is None:
            page = 1
        if per_page is None:
            per_page = 10

        key1 = Log.from_id == user_id
        key2 = Log.to_id == user_id

        result = Log.query.order_by(Log.create_time.desc()).filter(
            or_(
                key1,
                key2,
                # key3,
                # key4
            )
        )

        result = result.paginate(page=int(page), per_page=int(per_page))
        ans = {'data': result.items, 'pages': result.pages, 'total': result.total}

        return ans

    def getFuzzy(self, username=""):
        key1 = or_(Log.username.like("%" + username + "%"), Log.username.is_(None))
        # key2 = or_(UserInfo.id.like("%" + id + "%"), UserInfo.id.is_(None))
        # key3 = or_(UserInfo.email.like("%" + email + "%"), UserInfo.email.is_(None))
        # key4 = or_(UserInfo.location.like("%" + location + "%"), UserInfo.location.is_(None))

        if username is not "":
            key1 = Log.username.like("%" + username + "%")
        # if id is not "":
        #     key2 = UserInfo.id.like("%" + id + "%")
        # if email is not "":
        #     key3 = UserInfo.email.like("%" + email + "%")
        # if location is not "":
        #     key4 = UserInfo.location.like("%" + location + "%")

        result = Log.query.filter(
            and_(
                key1,
                # key2,
                # key3,
                # key4
            )
        )

        return result
