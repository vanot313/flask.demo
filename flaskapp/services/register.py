from flask import *
from application import db
from common.models.admin import Admin
from util.response import response
from application import db,app


class Register:
    def __init__(self):
        pass

    def register_admin(self, username, password, email, mobile):
        new = Admin(username=username, password=password, email=email, mobile=mobile)

        try:
            db.session.add(new)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("登陆成功", 200, new)

    def register_expert(self, username, password, email, mobile):
        new = Admin(username=username, password=password, email=email, mobile=mobile)

        try:
            db.session.add(new)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("登陆成功", 200, new)

