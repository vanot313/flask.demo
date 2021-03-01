# coding:utf-8
from flask import Blueprint, render_template, jsonify, request
from dao import dao_service
from util import str_tools
from util import response

import random

# 创建一个蓝图对象
data = Blueprint("data", __name__)


# 在生产环境中弃用
@data.route("/single", methods=['GET'])
def singleJudge():
    dict = {}

    count = 1
    time = 30000

    di = []
    while time > 0:
        d = {}

        randint = random.randint(0, 3)
        flag = (randint == 0)
        name = str_tools.ranstr(6)

        d['id'] = count
        d['flag'] = flag
        di.append(d)

        count = count + 1
        time = time - 1

    dict["data"] = di

    return dict


@data.route("/comprehensive", methods=['POST', 'GET'])
def comprehensive():
    pass


@data.route("/cost", methods=['POST'])
def cost():

    pass


@data.route("/earning", methods=['POST'])
def earning():

    pass
