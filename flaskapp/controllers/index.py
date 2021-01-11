# coding:utf-8
from flask import Blueprint, render_template, jsonify, request
from common.models.user import User
from common.models.account import Account
from services import companyDataService
from util import strTools
from services import csvHandler

import random

# 创建一个蓝图对象
data = Blueprint("data", __name__)


# 注册路由
@data.route("/", methods=['GET'])
def index():
    context = {}
    result = Account.query.all()
    # context['result'] = result
    title = 'WELCOME'
    context['title'] = title
    return jsonify(context)
    # return render_template("index.html", **context)c


# 在生产环境中弃用
@data.route("/single", methods=['GET'])
def singleJudge():
    # dict = companyDataService.single()

    dict = {}

    count = 1
    time = 30000

    di = []
    while time > 0:
        d = {}

        randint = random.randint(0, 3)
        flag = (randint == 0)
        name = strTools.ranstr(6)

        d['id'] = count
        d['flag'] = flag
        di.append(d)

        count = count + 1
        time = time - 1

    dict["data"] = di

    return dict


@data.route("/multiple", methods=['GET'])
def multipleJudge():
    csvHandler.buildVertifyFile()
    dict = companyDataService.multiple()

    return dict


@data.route("/getDataById", methods=['GET'])
def getDataByid():
    id = int(request.args.get('id'))
    dict = companyDataService.fenxi(id)
    return dict


