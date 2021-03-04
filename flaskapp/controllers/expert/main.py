# coding:utf-8
from flask import *
from services import *
import json
from application import db, app

# 创建一个蓝图对象
from util.response import response

expert = Blueprint("expert", __name__)


@expert.route("/login", methods=['GET', 'POST'])
def login_expert():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('name')
        password = request.form.get('password')

        return services_container.login_handler.login_expert(username, password)


@expert.route("/comprehensive", methods=['GET', 'POST'])
def comprehensive():
    if request.method == 'GET':
        # TODO 返回给专家用户上传的数据集

        pass
    else:
        order_id = request.form.get("order_id")

        rareness = request.form.get("rareness")
        timeliness = request.form.get("timeliness")
        dimensional = request.form.get("dimensional")
        economy = request.form.get("economy")

        quality_weight = json.loads(request.form.get("quality_weight"))
        applied_weight = json.loads(request.form.get("applied_weight"))

        return services_container.expert_handler.comprehensive_handler(order_id, rareness, timeliness, dimensional, economy, quality_weight, applied_weight)


@expert.route("/cost", methods=['GET', 'POST'])
def cost():
    if request.method == 'GET':
        # TODO 返回给专家用户指定的公司名称/数据集名称

        pass
    else:
        order_id = request.form.get("order_id")

        R = request.form.get("R")
        C = request.form.get("C")
        II = request.form.get("II")
        M = request.form.get("M")
        E = request.form.get("E")

        return services_container.expert_handler.cost_handler(order_id, R, C, II, M, E)


@expert.route("/earning", methods=['GET', 'POST'])
def earning():
    if request.method == 'GET':
        # TODO 返回给专家用户指定的公司名称/数据集名称

        pass
    else:
        order_id = request.form.get("order_id")

        n = request.form.get("n")
        r = request.form.get("r")
        R = json.loads(request.form.get("R"))

        return services_container.expert_handler.earning_handler(order_id, n, r, R)
