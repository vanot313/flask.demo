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

        print("********************************")
        print(result.check_password(password))

        if(result.check_password(password)):
            session['user_login'] = 1
            return "login success"
        else:
            return "login failed"