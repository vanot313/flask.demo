# coding:utf-8
from flask import Blueprint, render_template, jsonify
from common.models.user import User
from common.models.account import Account

# 创建一个蓝图对象
index_page = Blueprint("index_page", __name__)


# 注册路由，指定静态文件夹
@index_page.route("/")
def index():
    context = {}
    # result = User.query.all()
    result = Account.query.all()
    # context['result'] = result
    title = 'it works'
    context['title'] = title
    return jsonify(context)
    # return render_template("index.html", **context)
