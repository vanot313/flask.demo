from flask import *
from common.models import *
from dao import dao_service
from util.response import response
from application import db,app


class RegisterHandler:
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
            if dao_service.user_dao.getByName(username) is None:
                return response("用户名已存在", 301, {})
            dao_service.user_dao.add(new_user)
        except Exception as e:
            return response("数据库访问失败", 1001, {})


        try:
            new_user_info = UserInfo(id=new_user.id, username=username, email=email,
                                     mobile=mobile, birth=birth, location=location)
            dao_service.user_info_dao.add(new_user_info)
        except Exception as e:
            return response("数据库访问失败", 1001, {})

        return response("注册成功", 200, new_user_info)