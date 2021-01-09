# coding:utf-8
from flask import Blueprint, render_template, jsonify
from common.models.user import User
from common.models.account import Account
from services import companyDataService


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


@data.route("/single", methods=['GET'])
def singleJudge():

    dict = companyDataService.single()

    return dict


@data.route("/multiple", methods=['GET'])
def multipleJudge():

    dict = companyDataService.multiple()

    # dict = {}
    #
    # count = 1
    # time = 100
    #
    # di = []
    # while time > 0:
    #     tuple = []
    #
    #     randint = random.randint(0, 3)
    #     flag = (randint == 0)
    #     name = ranstr(6)
    #
    #     tuple.append(count)
    #     tuple.append(name)
    #     tuple.append(flag)
    #     di.append(tuple)
    #
    #     count = count + 1
    #     time = time - 1
    #
    # dict["data"] = di

    return dict


