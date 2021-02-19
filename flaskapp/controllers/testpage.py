# coding:utf-8
from flask import *

from application import db
from common.models.user import User
from common.models.account import Account
import random
from util import strTools


testpage = Blueprint("testpage", __name__)

@testpage.route("/welcome", methods=['GET'])
def index():
    context = {}
    result = Account.query.all()
    # context['result'] = result
    title = 'WELCOME'
    context['title'] = title
    return jsonify(context)

@testpage.route("/", methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        name = strTools.ranstr(6)
        # 新增用户
        new = Account(name=name, password='123')

        db.session.add(new)
        db.session.commit()

        return "test pass"
    else:
        pass
