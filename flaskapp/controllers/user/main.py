from flask import *
from services.login import Login
from services.upload import Uploader
from services.register import Register
from util.response import *
from dao import dao_service
from application import app
from common.models.user import User
from config.method_setting import *
from services.login import LoginHandler
from services.process.user_handler import *

user = Blueprint("user", __name__)


@user.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        l = LoginHandler()

        if l.is_login():
            return render_template("index.html")

        return render_template("login.html")

    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        l = LoginHandler()
        l.login_user(name, password)

        return redirect(request.args.get('next') or url_for('user.comprehensive_upload'))
        # return l.login_user(name, password)


@user.route('/detail', methods=['GET'])
def getUser():
    try:
        id = request.args.get('id')
        return response("success", 200, dao_service.user_dao.getById(id))
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
            return response("添加成功", 200, dao_service.user_dao.update(user))
        except Exception as e:
            app.logger.info("Exception: %s", e)
            return response('失败', 1001, {})


@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        # id = request.form.get('user_id')
        name = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        # avatar = request.form.get('avatar')
        # description = request.form.get('description')
        location = request.form.get('location')
        birth = request.form.get('birth')

        r = Register()
        return r.register_user(name, password, email, mobile, location, birth)



@user.route('/getinfo', methods=['GET'])
def get_info():
    info = session.get('id')
    dict = {}
    dict["id"] = info
    return dict


@user.route('/logout', methods=['GET'])
def logout():
    l = LoginHandler()

    return l.logout()

    # return render_template("login.html")


@user.route('/costupload', methods=['POST', 'GET'])
def cost_upload():
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        method = COST
        user_id = session.get("id")

        return UserCostHandler(user_id, remarks, method)


@user.route('/earningupload', methods=['POST', 'GET'])
def earning_upload():
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        method = EARNING
        user_id = session.get("id")

        return UserEarningHandler(user_id, remarks, method)


@user.route('/comprehensiveupload', methods=['POST', 'GET'])
def comprehensive_upload():
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        u = Uploader()
        remarks = request.form.get('remarks')
        file = request.files['file']
        filename = u.upload_single(file)
        method = COMPREHENSIVE
        user_id = session.get("id")

        if file is not None:
            return UserComprehensiveHandler(user_id, remarks, method, filename)
        else:
            return response('上传失败', 1001, {})


@user.route('/s', methods=['POST', 'GET'])
def s():
    return response_multiple('test', 0, dao_service.user_dao.getById(3))
