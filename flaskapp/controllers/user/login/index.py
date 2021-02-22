import common.models.user
from flask import *
from application import db
from common.models.user import User
from common.models.account import Account
import random
from util import strTools, response
import subprocess

user_login = Blueprint("user_login", __name__)


@user_login.route("/status", methods=['POST'])
def login():
    name = request.form.get('username')
    password = request.form.get('password')
    result = User.query.filter(User.username == name).first()
    if result == None:
        return response.response("login fail", 200, {})
    else:
        return response.response("login success", 200, result)