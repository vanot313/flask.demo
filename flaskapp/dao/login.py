from datetime import datetime
from common.models.login import Login
from application import db


class LoginDao:
    def getById(self, id):
        result = Login.query.filter(Login.id == int(id)).filter(Login.status == 0).first()
        return result

    def getAll(self):
        result = Login.query.all()
        return result

    def getByName(self, name):
        result = Login.query.filter(Login.username == name)
        return result
