from flask import *
from services import *
from util.response import *
from util.permission import *
from dao import dao_service
from config.macro_setting import *

user = Blueprint("user", __name__)


# 登录
@user.route("/login", methods=['POST', 'GET'])
def login():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        if services_container.login_handler.is_login():
            return dao_service.user_info_dao.getById(session.get('id')).first()

        return render_template("login.html")

    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        return services_container.login_handler.login_user(name, password)
        # return redirect(request.args.get('next') or url_for('user.index'))


# 登出 注销 session
@user.route('/logout', methods=['GET'])
@permission_required(USER)
def logout():
    return services_container.login_handler.logout()


# 获取个人信息(当前用户)
@user.route('/detail', methods=['GET'])
@permission_required(USER)
def detail():
    id = request.args.get('id')
    # print(dao_service.user_info_dao.getById(session.get('id')))
    return response("success", 200, dao_service.user_info_dao.getById(id))


# 注册
@user.route('/register', methods=['POST', 'GET'])
def register():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        # id = request.form.get('user_id')
        name = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        mobile = request.form.get('phoneNum')
        # avatar = request.form.get('avatar')
        description = request.form.get('introduction')
        location = request.form.get('location')
        birth = request.form.get('birth')
        sex = request.form.get('sex')

        return services_container.register_handler.register_user(name, password, email, mobile, location, birth,
                                                                 description, sex)


# 修改个人信息
@user.route('/update', methods=['POST', 'GET'])
@permission_required(USER)
def update():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("update.html")

    if request.method == 'POST':
        email = request.form.get('email')
        mobile = request.form.get('phoneNum')
        location = request.form.get('location')
        birth = request.form.get('birth')
        description = request.form.get('introduction')
        sex = request.form.get('sex')
        username = request.form.get('username')
        id = request.form.get('id')
        return services_container.user_handler.update_info(id, username, sex, email, mobile, location, birth,
                                                           description)


# 提交工单
def new_cost(request):
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        method = COST
        name = request.form.get('username')

        result = dao_service.user_info_dao.getByName(name)
        user_id = result.id

        expert_id = request.form.get("expert_id")
        if expert_id is None:
            expert_id = 0

        return services_container.user_handler.cost_handler(user_id, remarks, method, expert_id)


def new_earning(request):
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("test.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        method = EARNING
        name = request.form.get('username')
        result = dao_service.user_info_dao.getByName(name)
        expert_id = request.form.get('expert_id')

        if expert_id is None:
            expert_id = 0

        user_id = result.id

        return services_container.user_handler.earning_handler(user_id, remarks, method, expert_id)


def new_comprehensive(request):
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("upload.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        file = request.files['file']
        method = COMPREHENSIVE
        expert_id = request.form.get('expert_id')

        if expert_id is None:
            expert_id = 0

        if session.get("id") is None:
            name = request.form.get('username')
            result = dao_service.user_info_dao.getByName(name)
            user_id = result.id
        else:
            user_id = session.get("id")

        if file is not None:
            filename = file.filename
            filepath = services_container.file_handler.upload_single(file, "comprehensive")
            return services_container.user_handler.comprehensive_handler(user_id, remarks, method, filepath, filename, expert_id)
        else:
            return response('上传失败', 1001, {})


def new_market(request):
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("upload.html")

    if request.method == 'POST':
        remarks = request.form.get('remarks')
        file = request.files['file']
        method = MARKET

        user_id = session.get("id")
        expert_id = request.form.get('expert_id')
        if expert_id is None:
            expert_id = 0

        if file is not None:
            filename = file.filename
            filepath = services_container.file_handler.upload_single(file, "market")
            return services_container.user_handler.market_handler(user_id, remarks, method,
                                                                  filepath, filename, expert_id)
        else:
            return response('上传失败', 1001, {})


@user.route('/new_work', methods=['POST'])
@permission_required(USER)
def new_work():
    method = request.form.get('method')
    if method == '1':
        return new_cost(request)
    elif method == '2':
        return new_earning(request)
    elif method == '3':
        return new_comprehensive(request)
    elif method == '4':
        return new_market(request)
    return response('创建失败', 1002, {})


# 查看所有工单
@user.route('/all_work_order', methods=['GET'])
@permission_required(USER)
def work_order_all():
    # user_id = request.form.get('id')
    user_id = session.get('id')
    return response_multiple("查询成功", 200, dao_service.work_order_dao.getByUserId(user_id))


# 查看工单详情
@user.route('/detail_work_order', methods=['GET', 'POST'])
@permission_required(USER)
def work_order_detail():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("detail.html")

    if request.method == 'POST':
        order_id = request.form.get('order_id')
        return services_container.data_handler.get_work_order_detail_by_id(order_id)


@user.route('/get_all_user', methods=['GET'])
@permission_required(USER)
def get_all_user():
    return services_container.user_handler.get_all_user()


@user.route('/get_all_expert', methods=['GET'])
@permission_required(USER)
def get_all_expert():
    return services_container.user_handler.get_all_expert()


'''
# 智扬写的更新用户信息 保留
@user.route('/update_user', methods=['POST'])
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
            
            
工单申请具体流程：
1.进入到前端界面
2.填写 
    选择专家  访问 user/get_all_expert 接口获取专家信息
    选择方法  具体调用接口 user/new_work
            成本法、收益法不需要传文件     综合市场法要传文件 
                参数 file 文件类型为csv
            成本法创建  '1'
            收益法创建  '2'
            综合估值法  '3'
            市场法     '4'
            其他参数
                username 用户名 string
                remarks  备注 string
                method   选择方法 string
                expert_id 专家id int（可以不选择，不选择则不上传该参数，或者将其置为0）
3.查看全部工单 简略信息  user/all_work_order 
    参数 id 用户id
4.具体查看某一个工单  user/detail_work_order
    参数 order_id 工单的id


'''
