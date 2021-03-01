from flask import *
from common.models.admin_info import AdminInfo
from common.models.expert_info import ExpertInfo
from common.models.user import User
from common.models.user_info import UserInfo
from util.response import response
from application import db,app


class Register:
    def __init__(self):
        pass

    # 在现行逻辑下即将被弃用
    def register_admin(self, username, password, email, mobile):
        new = AdminInfo(username=username, password=password, email=email, mobile=mobile)

        try:
            db.session.add(new)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("注册成功", 200, new)

    # 在现行逻辑下即将被弃用
    def register_expert(self, username, password, email, mobile):
        new = ExpertInfo(username=username, password=password, email=email, mobile=mobile)

        try:
            db.session.add(new)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("注册成功", 200, new)

    def register_user(self, username, password, email, mobile, location, birth):
        new_user = User(username=username, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        new_user_info = UserInfo(id=new_user.id, username=username, email=email,
                                 mobile=mobile, birth=birth, location=location)
        try:
            db.session.add(new_user_info)
            db.session.commit()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("注册成功", 200, new_user_info)