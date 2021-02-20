# coding:utf-8
from flask import *
from common.models.account import Account

# 创建一个蓝图对象
main = Blueprint("main", __name__)

@main.route("/login", methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return render_template("test.html")
    else:
        name = request.form.get('name')
        password = request.form.get('password')

        result = Account.query.filter(Account.name == name).first()

        if(result == None):
            dict = {}
            dict["code"] = 2
            dict["msg"] = "登陆失败"
            return dict

        if(result.check_password(password)):
            session['user_login'] = 1
            dict = {}
            dict["code"] = 1
            dict["msg"]= "登陆成功"
            return dict
        else:
            dict = {}
            dict["code"] = 0
            dict["msg"] = "登陆失败"
            return dict