from flask import *
from application import app
from common.models import *
from util.response import response
from dao import dao_service


class LoginHandler:
    def __init__(self):
        pass

    def login_user(self, username, password):
        try:
            result = Login.query.filter(Login.username == username and Login.rolename == "admin").first()

            if result is None:
                return response("登陆失败", 1001, {})
            elif result.check_password(password):
                session['id'] = result.id

                new_log = LoginLog(username=username, rolename="user")
                dao_service.login_log_dao.add(new_log)

                return response("登陆成功", 200, result)
            else:
                return response("登陆失败", 1001, {})

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

    def login_admin(self, username, password):
        try:
            result = Login.query.filter(Login.username == username and Login.rolename == "admin").first()

            if result is None:
                return response("登陆失败", 200, {})
            elif result.check_password(password):
                session['id'] = result.id

                new_log = LoginLog(username=username, rolename="admin")
                dao_service.login_log_dao.add(new_log)

                return response("登陆成功", 200, result)
            else:
                return response("登陆失败", 1001, {})

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

    def login_expert(self, username, password):
        try:
            result = Login.query.filter(Login.username == username and Login.rolename == "expert").first()

            if result is None:
                return response("登陆失败", 1001, {})
            elif result.check_password(password):
                session['id'] = result.id

                new_log = LoginLog(username=username, rolename="expert")
                dao_service.login_log_dao.add(new_log)

                return response("登陆成功", 200, result)
            else:
                return response("登陆失败", 1001, {})

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

    def is_login(self):
        if session.get('id') is not None:
            return True
        return False

    def logout(self):
        session.clear()

        return response("登出成功", 200, {})
