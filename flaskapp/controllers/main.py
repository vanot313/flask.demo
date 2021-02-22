# coding:utf-8
from flask import *
from common.models.admin import admin
from services.register import register
from services.login import login

# 创建一个蓝图对象
main = Blueprint("main", __name__)


@main.route("/login_admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('name')
        password = request.form.get('password')

        l = login()
        msg = l.login_admin(username, password)
        return msg

@main.route("/register_admin", methods=['GET', 'POST'])
def register_admin():
    if request.method == 'GET':
        return render_template("test.html")
    else:
        username = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        mobile = request.form.get('mobile')

        r = register()
        msg = r.register_admin(username, password, email, mobile)

        # result = Account.query.filter(Account.name == name).first()
        #
        # if(result == None):
        #     dict = {}
        #     dict["code"] = 2
        #     dict["msg"] = "登陆失败"
        #     return dict
        #
        # if(result.check_password(password)):
        #     session['user_login'] = 1
        #     dict = {}
        #     dict["code"] = 1
        #     dict["msg"]= "登陆成功"
        #     return dict
        # else:
        #     dict = {}
        #     dict["code"] = 0
        #     dict["msg"] = "登陆失败"
        #     return dict
        return msg
