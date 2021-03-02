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

        msg = services_container.login_handler.login_expert(username, password)
        return msg


@expert.route("/register", methods=['GET', 'POST'])
def register_expert():
    if request.method == 'GET':
        return render_template("test.html")


@expert.route("/comprehensive", methods=['GET', 'POST'])
def comprehensive():
    if request.method == 'GET':
        # TODO 返回给专家用户上传的数据集

        pass
    else:
        work_order_id = request.form.get("work_order_id")

        rareness = request.form.get("rareness")
        timeliness = request.form.get("timeliness")
        dimensional = request.form.get("dimensional")
        economy = request.form.get("economy")

        quality_weight = json.loads(request.form.get("quality_weight"))
        applied_weight = json.loads(request.form.get("applied_weight"))

        try:
            services_container.expert_handler.ComprehensiveHandler(work_order_id, rareness, timeliness, dimensional, economy, quality_weight, applied_weight)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("成功", 200, {})


@expert.route("/cost", methods=['GET', 'POST'])
def cost():
    if request.method == 'GET':
        # TODO 返回给专家用户指定的公司名称/数据集名称

        pass
    else:
        work_order_id = request.form.get("work_order_id")

        R = request.form.get("R")
        C = request.form.get("C")
        II = request.form.get("II")
        M = request.form.get("M")
        E = request.form.get("E")

        try:
            services_container.expert_handler.CostHandler(work_order_id, R, C, II, M, E)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("成功", 200, {})


@expert.route("/earning", methods=['GET', 'POST'])
def earning():
    if request.method == 'GET':
        # TODO 返回给专家用户指定的公司名称/数据集名称

        pass
    else:
        work_order_id = request.form.get("work_order_id")

        n = request.form.get("n")
        r = request.form.get("r")
        R = json.loads(request.form.get("R"))

        try:
            services_container.expert_handler.EarningHandler(work_order_id, n, r, R)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("成功", 200, {})
