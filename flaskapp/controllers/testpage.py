# coding:utf-8
from flask import *

from application import db
from common.models import *
import random
import common.models
from common.models.admin import admin
from util import strTools

testpage = Blueprint("testpage", __name__)


@testpage.route("/welcome", methods=['GET'])
def index():
    context = {}
    result = admin.query.all()
    # context['result'] = result
    title = 'WELCOME'
    context['title'] = title
    return jsonify(context)


@testpage.route("/", methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return render_template("test.html")
        # name = strTools.ranstr(6)
        # # 新增用户
        # new = Account(name=name, password='123')
        #
        # db.session.add(new)
        # db.session.commit()
        #
        # return "test pass"
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        mobile = request.form.get('mobile')

        new = admin(username=name, password=password, email=email, mobile=mobile)

        db.session.add(new)
        db.session.commit()

        return "test pass"
