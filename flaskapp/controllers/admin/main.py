from flask import *
from flask_cors import CORS
from services import *
from util.response import *
from util.permission import *
from common.models import *
from dao import dao_service
from application import app
from config.macro_setting import *

# 创建一个蓝图对象
admin = Blueprint("admin", __name__)


@admin.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if services_container.login_handler.is_login():
            return dao_service.admin_info_dao.getById(session.get('id')).first()

        return render_template("login.html")
    else:

        data = request.get_json(silent=True)

        username = data['username']
        password = data['password']


        return services_container.login_handler.login_admin(username, password)


# 登出 注销 session
@admin.route('/logout', methods=['GET'])
@permission_required(ADMIN)
def logout():
    return services_container.login_handler.logout()


@admin.route("/detail", methods=['GET'])
@permission_required(ADMIN)
def detail():
    return response("success", 200, dao_service.admin_info_dao.getById(session.get('id')).first())


# 修改个人信息
@admin.route('/update_info', methods=['POST', 'GET'])
@permission_required(ADMIN)
def update_info():
    if request.method == 'GET':
        return render_template("update.html")

    if request.method == 'POST':
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        location = request.form.get('location')
        birth = request.form.get('birth')
        description = request.form.get('description')

        return services_container.admin_handler.update_info(email, mobile, location, birth, description)


# 查询用户信息
@admin.route('/get_user_info', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_user_info():
    if request.method == 'GET':
        return response_multiple("查询成功", 200, dao_service.user_info_dao.getAll())

    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('username')
        email = request.form.get('email')
        location = request.form.get('location')

        return response_multiple("查询成功", 200, dao_service.user_info_dao.getFuzzy(id, name, email, location))


@admin.route('/update_user_info', methods=['POST'])
@permission_required(ADMIN)
def update_user_info():
    id = request.form.get('id')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    birth = request.form.get('birth')
    description = request.form.get('description')
    location = request.form.get('location')

    return services_container.admin_handler.update_user_info(id, email, mobile, location, birth, description)


@admin.route('/get_work_order', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_work_order():
    if request.method == 'GET':
        return response_multiple("查询成功", 200, dao_service.work_order_dao.getAll())

    if request.method == 'POST':
        order_id = request.form.get('order_id')
        return dao_service.work_order_dao.getFuzzy(order_id)


@admin.route('/get_login_log', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_login_log():
    if request.method == 'GET':
        return response_multiple("查询成功", 200, dao_service.login_log_dao.getAll())

    if request.method == 'POST':
        username = request.form.get('username')
        return dao_service.login_log_dao.getFuzzy(username)


@admin.route('/get_log', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_log():
    if request.method == 'GET':
        return response_multiple("查询成功", 200, dao_service.log_dao.getAll())

    if request.method == 'POST':
        username = request.form.get('username')
        return dao_service.log_dao.getFuzzy(username)
