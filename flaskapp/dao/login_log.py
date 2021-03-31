import json
from datetime import datetime

from sqlalchemy import *

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

    def getFuzzy(self, username="", page="1", per_page="10"):
        if page is None:
            page = 1
        if per_page is None:
            per_page = 10
        if username is None:
            username = ''

        key1 = or_(LoginLog.username.like("%" + username + "%"), LoginLog.username.is_(None))
        # key2 = or_(UserInfo.id.like("%" + id + "%"), UserInfo.id.is_(None))
        # key3 = or_(UserInfo.email.like("%" + email + "%"), UserInfo.email.is_(None))
        # key4 = or_(UserInfo.location.like("%" + location + "%"), UserInfo.location.is_(None))

        if username is not "":
            key1 = LoginLog.username.like("%" + username + "%")
        # if id is not "":
        #     key2 = UserInfo.id.like("%" + id + "%")
        # if email is not "":
        #     key3 = UserInfo.email.like("%" + email + "%")
        # if location is not "":
        #     key4 = UserInfo.location.like("%" + location + "%")

        result = LoginLog.query.order_by(LoginLog.login_time.desc()).filter(
            and_(
                key1,
                # key2,
                # key3,
                # key4
            )
        )

        result = result.paginate(page=int(page), per_page=int(per_page))
        ans = {}
        ans['data'] = result.items
        ans['pages'] = result.pages
        ans['total'] = result.total

        return ans