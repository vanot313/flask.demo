import common.models.user
from flask import *
from services.login import login_user
from util.response import response
from services.user import add, update, getById, getByName
from application import app
from common.models.user import User

user = Blueprint("user_login", __name__)


@user.route("/login/status", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        return login_user(name, password)


@user.route('/detail', methods=['GET'])
def getUser():
    try:
        id = request.args.get('id')
        return response("success", 200, getById(id))
    except Exception as e:
        app.logger.info("Exception: %s", e)
        return response('失败', 1001, {})


@user.route('/update', methods=['POST'])
def updateUser():
    json_data = request.get_json()
    if json_data is not None:
        # 注册用户
        user = User.from_json(json_data)
        try:
            return response("添加成功", 200, update(user))
        except Exception as e:
            app.logger.info("Exception: %s", e)
            return response('失败', 1001, {})


@user.route('/register', methods=['POST'])
def register():
    id = request.form.get('user_id')
    name = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    #avatar = request.form.get('avatar')
    #description = request.form.get('description')
    # location = request.form.get()
    # birth = request.form.get()
    # 注册用户
    user = User(user_id=id, username=name, password=password, email=email, mobile=mobile)
    try:
        return response("添加成功", 200, add(user))
    except Exception as e:
        app.logger.info("Exception: %s", e)
        return response('失败', 1001, {})
