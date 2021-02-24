from flask import *
from application import db,app
from common.models.admin import Admin
from common.models.user import User
from util.response import response


def login_user(username, password):
    try:
        result = User.query.filter(User.username == username).first()
    except Exception as e:
        app.logger.info('Exception: %s', e)
        return response("失败", 1001, {})

    if result is None:
        return response("登陆失败", 200, {})
    elif result.check_password(password):
        return response("登陆成功", 200, result)
    else:
        return response("登陆失败", 200, {})


class Login:
    def __init__(self):
        pass

    def login_admin(self, username, password):
        try:
            result = Admin.query.filter(Admin.username == username).first()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        if result is None:
            return response("登陆失败", 200, {})
        elif result.check_password(password):
            return response("登陆成功", 200, result)
        else:
            return response("登陆失败", 200, {})

    def login_expert(self, username, password):
        try:
            result = Admin.query.filter(Admin.username == username).first()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        if result is None:
            return response("登陆失败", 200, {})
        elif result.check_password(password):
            return response("登陆成功", 200, result)
        else:
            return response("登陆失败", 200, {})
