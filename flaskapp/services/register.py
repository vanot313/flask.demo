from flask import *
from application import db
from common.models.admin import admin


class register:
    def __init__(self):
        pass

    def register_admin(self, username, password, email, mobile):
        new = admin(username=username, password=password, email=email, mobile=mobile)

        db.session.add(new)
        db.session.commit()

        dict = {}
        dict["code"] = 1
        dict["msg"] = "注册成功"

        return dict
