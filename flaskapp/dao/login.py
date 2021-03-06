from datetime import datetime
from sqlalchemy import *
from common.models.login import Login
from application import db


class LoginDao:
    def getByNameAndRole(self, username, rolename):
        result = Login.query.filter(
            and_(
                Login.username == username,
                Login.rolename == rolename
            )
        ).filter(Login.status == 0).first()
        return result

    def getAll(self):
        result = Login.query.all()
        return result

    def getByName(self, name):
        result = Login.query.filter(Login.username == name)
        return result
