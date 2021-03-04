from flask import *
from services import *
from util.response import *
from dao import dao_service
from application import app
from common.models import *
from config.method_setting import *

user = Blueprint("user", __name__)


@user.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html",
                               resp=dao_service.user_info_dao.getById(session.get('id')).first())


# 登录
@user.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if services_container.login_handler.is_login():
            return render_template("index.html",
                                   resp=dao_service.user_info_dao.getById(session.get('id')).first())
        return render_template("login.html")

    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        return services_container.login_handler.login_user(name, password)
        # return redirect(request.args.get('next') or url_for('user.index'))


# 注册
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

        return services_container.register_handler.register_user(name, password, email, mobile, location, birth)


# 修改个人信息
@user.route('/update_userinfo', methods=['POST', 'GET'])
def update_userinfo():
    if request.method == 'GET':
        return render_template("update.html")

    if request.method == 'POST':
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        location = request.form.get('location')
        birth = request.form.get('birth')
        description = request.form.get('description')

        return services_container.user_handler.update_info(email, mobile, location, birth, description)


# 获取个人信息(当前用户)
@user.route('/detail', methods=['GET'])
def getUser():
    return response("success", 200, dao_service.user_info_dao.getById(session.get('id')).first())


# 登出 注销 session
@user.route('/logout', methods=['GET'])
def logout():
    return services_container.login_handler.logout()


# 提交工单
@user.route('/costd', methods=['POST', 'GET'])
def cost():
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        method = COST
        user_id = session.get("id")

        return services_container.user_handler.cost_handler(user_id, remarks, method)


@user.route('/earning', methods=['POST', 'GET'])
def earning():
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        method = EARNING
        user_id = session.get("id")

        return services_container.user_handler.earning_handler(user_id, remarks, method)


@user.route('/comprehensive', methods=['POST', 'GET'])
def comprehensive():
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        file = request.files['file']
        filename = services_container.upload_handler.upload_single(file)
        method = COMPREHENSIVE
        user_id = session.get("id")

        if file is not None:
            return services_container.user_handler.comprehensive_handler(user_id, remarks, method, filename)
        else:
            return response('上传失败', 1001, {})


# 查看所有工单
@user.route('/work_order_all', methods=['GET'])
def work_order_all():
    user_id = session.get('id')
    return response_multiple("查询成功", 200, dao_service.work_order_dao.getByUserId(user_id))


# 查看工单详情
@user.route('/work_order_detail', methods=['GET', 'POST'])
def work_order_detail():
    if request.method == 'GET':
        return render_template("detail.html")

    if request.method == 'POST':
        order_id = request.form.get('order_id')
        return services_container.data_handler.get_work_order_detail_by_id(order_id)


# TODO 完成该逻辑
# 申请专家权限
@user.route('/apply_expert', methods=['GET', 'POST'])
def apply_expert():
    pass


# 智扬写的更新用户信息 保留
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
