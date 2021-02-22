from flask import *
from application import db
from common.models.admin import admin


class login:
    def __init__(self):
        pass

    def login_admin(self, username, password):
        result = admin.query.filter(admin.username == username).first()

        if (result == None):
            dict = {}
            dict["code"] = 0
            dict["msg"] = "登陆失败"
            return dict

        if (result.check_password(password)):
            session['user_login'] = 1
            dict = {}
            dict["code"] = 1
            dict["msg"] = "登陆成功"
            return dict
        else:
            dict = {}
            dict["code"] = 0
            dict["msg"] = "登陆失败"
            return dict

