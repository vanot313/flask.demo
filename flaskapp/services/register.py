from flask import *
from common.models.admin_info import AdminInfo
from common.models.expert_info import ExpertInfo
from util.response import response
from application import db,app


class Register:
    def __init__(self):
        pass

    def register_admin(self, username, password, email, mobile):
        new = AdminInfo(username=username, password=password, email=email, mobile=mobile)

        try:
            db.session.add(new)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("注册成功", 200, new)

    def register_expert(self, username, password, email, mobile):
        new = ExpertInfo(username=username, password=password, email=email, mobile=mobile)

        try:
            db.session.add(new)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("注册成功", 200, new)

