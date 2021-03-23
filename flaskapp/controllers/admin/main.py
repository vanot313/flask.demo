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
            return redirect(url_for('admin.detail'))
        return render_template('login.html')
    else:
        try:
            data = request.get_json(silent=True)

            if data is not None:
                username = data.get('username')
                password = data.get('password')

            else:
                username = request.form.get('username')
                password = request.form.get('password')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return services_container.login_handler.login_admin(username, password)


# 登出 注销 session
@admin.route('/logout', methods=['GET'])
@permission_required(ADMIN)
def logout():
    return services_container.login_handler.logout()


@admin.route("/detail", methods=['GET'])
@permission_required(ADMIN)
def detail():
    data = response("success", 200, dao_service.admin_info_dao.getById(session.get('id')).first())

    return response("success", 200, dao_service.admin_info_dao.getById(session.get('id')).first())


# 修改个人信息
@admin.route('/update', methods=['POST', 'GET'])
@permission_required(ADMIN)
def update():
    if request.method == 'GET':
        return render_template('update.html')
    else:
        try:
            data = request.get_json(silent=True)

            if data is not None:
                birth = data.get('birth')
                location = data.get('location')
                description = data.get('description')
                email = data.get('email')
                mobile = data.get('mobile')

            else:
                email = request.form.get('email')
                mobile = request.form.get('mobile')
                location = request.form.get('location')
                birth = request.form.get('birth')
                description = request.form.get('description')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return services_container.admin_handler.update_info(email, mobile, location, birth, description)


# 查询用户信息
@admin.route('/get_user_info', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_user_info():
    if request.method == 'GET':
        return render_template('get.html')
        # return response_multiple("查询成功", 200, dao_service.user_info_dao.getAll())

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                id = data.get('id')
                location = data.get('location')
                username = data.get('username')
                email = data.get('email')
                page = data.get('page')
                per_page = data.get('per_page')

            else:
                id = request.form.get('id')
                email = request.form.get('email')
                location = request.form.get('location')
                username = request.form.get('username')
                page = request.form.get('page')
                per_page = request.form.get('per_page')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return response_dict("查询成功", 200, dao_service.user_info_dao.getFuzzy(id, username, email, location, page, per_page))


@admin.route('/update_user_info', methods=['POST'])
@permission_required(ADMIN)
def update_user_info():
    try:
        data = request.get_json(silent=True)

        if data is not None:
            id = data.get('id')
            birth = data.get('birth')
            location = data.get('location')
            description = data.get('description')
            email = data.get('email')
            mobile = data.get('mobile')

        else:
            id = request.form.get('id')
            birth = request.form.get('birth')
            location = request.form.get('location')
            description = request.form.get('description')
            email = request.form.get('email')
            mobile = request.form.get('mobile')

    except Exception as e:
        app.logger.info('Exception: %s', e)
        return response("数据接收异常", 1002, {})

    return services_container.admin_handler.update_user_info(id, email, mobile, location, birth, description)


@admin.route('/get_work_order', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_work_order():
    if request.method == 'GET':
        # return response_multiple("查询成功", 200, dao_service.work_order_dao.getAll())
        return render_template("get.html")

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                order_id = data.get('order_id')
                page = data.get('page')
                per_page = data.get('per_page')

            else:
                order_id = request.form.get('order_id')
                page = request.form.get('page')
                per_page = request.form.get('per_page')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return response_dict("查询成功", 200, dao_service.work_order_dao.getFuzzy(order_id=order_id, page=page, per_page=per_page))


@admin.route('/get_login_log', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_login_log():
    if request.method == 'GET':
        return render_template("get.html")
        # return response_multiple("查询成功", 200, dao_service.login_log_dao.getAll())

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                username = data.get('username')
                page = data.get('page')
                per_page = data.get('per_page')

            else:
                username = request.form.get('username')
                page = request.form.get('page')
                per_page = request.form.get('per_page')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return response_dict("查询成功", 200, dao_service.login_log_dao.getFuzzy(username, page, per_page))


@admin.route('/get_log', methods=['POST', 'GET'])
@permission_required(ADMIN)
def get_log():
    if request.method == 'GET':
        # return render_template("get.html")
        return response_multiple("查询成功", 200, dao_service.log_dao.getAll())

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                username = data.get('username')
                page = data.get('page')
                per_page = data.get('per_page')

            else:
                username = request.form.get('username')
                page = request.form.get('page')
                per_page = request.form.get('per_page')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return response_multiple("查询成功", 200, dao_service.log_dao.getFuzzy(username, page, per_page))
