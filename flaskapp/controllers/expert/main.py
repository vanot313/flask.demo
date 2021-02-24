# coding:utf-8
from flask import *
from services.register import Register
from services.login import Login

# 创建一个蓝图对象
expert = Blueprint("expert", __name__)


@expert.route("/login", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('name')
        password = request.form.get('password')

        l = Login()
        msg = l.login_expert(username, password)
        return msg


@expert.route("/register", methods=['GET', 'POST'])
def register_admin():
    if request.method == 'GET':
        return render_template("test.html")
    else:
        username = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        mobile = request.form.get('mobile')

        r = Register()
        msg = r.register_expert(username, password, email, mobile)
        return msg
