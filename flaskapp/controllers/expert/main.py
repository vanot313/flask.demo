# coding:utf-8
from flask import *
from services.register import Register
from services.login import Login
import json

# 创建一个蓝图对象
expert = Blueprint("expert", __name__)


@expert.route("/login", methods=['GET', 'POST'])
def login_expert():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('name')
        password = request.form.get('password')

        l = Login()
        msg = l.login_expert(username, password)
        return msg


@expert.route("/register", methods=['GET', 'POST'])
def register_expert():
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


@expert.route("/comprehensive", methods=['GET', 'POST'])
def comprehensive():
    if request.method == 'GET':
        pass
    else:
        work_order_id = request.form.get("work_order_id")

        rareness = request.form.get("rareness")
        timeliness = request.form.get("timeliness")
        dimensional = request.form.get("dimensional")
        economy = request.form.get("economy")

        quality_weight = json.loads(request.form.get("quality_weight"))
        applied_weight = json.loads(request.form.get("applied_weight"))


