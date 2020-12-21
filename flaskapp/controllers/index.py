# coding:utf-8
from flask import Blueprint, render_template, jsonify
from common.models.user import User
from common.models.account import Account

# 创建一个蓝图对象
data = Blueprint("data", __name__)


# 注册路由
@data.route("/", methods=['GET'])
def index():
    context = {}
    result = Account.query.all()
    # context['result'] = result
    title = 'it works'
    context['title'] = title
    return jsonify(context)
    # return render_template("index.html", **context)

@data.route("/a", methods=['GET'])
def a():
    context = {}
    # result = User.query.all()
    result = Account.query.all()
    # context['result'] = result
    title = 'ohhhh'
    context['title'] = title
    return jsonify(context)
    # return render_template("index.html", **context)
