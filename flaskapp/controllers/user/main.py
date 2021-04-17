from flask import *
from services import *
from util.response import *
from util.permission import *
from dao import dao_service
from application import app
from config.macro_setting import *

user = Blueprint("user", __name__)


# 登录
@user.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if services_container.login_handler.is_login():
            return redirect(url_for('user.detail'))
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
            return response("数据接收异常", 1002, {})

        return services_container.login_handler.login_user(username, password)


# 登出 注销 session
@user.route('/logout', methods=['GET'])
@permission_required(USER)
def logout():
    return services_container.login_handler.logout()


# 获取个人信息(当前用户)
@user.route('/detail', methods=['GET'])
@permission_required(USER)
def detail():
    return response("success", 200, dao_service.user_info_dao.getById(session.get('id')).first())


# 注册
@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                username = data.get('username')
                password = data.get('password')
                email = data.get('email')
                mobile = data.get('mobile')
                location = data.get('location')
                birth = data.get('birth')

            else:
                username = request.form.get('username')
                password = request.form.get('password')
                email = request.form.get('email')
                mobile = request.form.get('mobile')
                location = request.form.get('location')
                birth = request.form.get('birth')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return services_container.register_handler.register_user(username, password, email, mobile, location, birth)


# 修改个人信息
@user.route('/update', methods=['POST', 'GET'])
@permission_required(USER)
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

        return services_container.user_handler.update_info(email, mobile, location, birth, description)


# 提交工单
@user.route('/new_cost', methods=['POST', 'GET'])
@permission_required(USER)
def new_cost():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("new_cost.html")

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                remarks = data.get('remarks')
                method = COST

                user_id = session.get("id")

                expert_id = data.get("expert_id")
                if expert_id is None:
                    expert_id = 0


            else:
                remarks = request.form.get('remarks')
                method = COST

                user_id = session.get("id")

                expert_id = request.form.get("expert_id")
                if expert_id is None:
                    expert_id = 0

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return services_container.user_handler.cost_handler(user_id, remarks, method, expert_id)


@user.route('/new_earning', methods=['POST', 'GET'])
@permission_required(USER)
def new_earning():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("new_cost.html")

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                remarks = data.get('remarks')
                method = EARNING

                user_id = session.get("id")

                expert_id = data.get("expert_id")
                if expert_id is None:
                    expert_id = 0


            else:
                remarks = request.form.get('remarks')
                method = EARNING

                user_id = session.get("id")

                expert_id = request.form.get("expert_id")
                if expert_id is None:
                    expert_id = 0

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return services_container.user_handler.earning_handler(user_id, remarks, method, expert_id)


@user.route('/new_comprehensive', methods=['POST', 'GET'])
@permission_required(USER)
def new_comprehensive():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        return render_template("new_comprehensive.html")

    if request.method == 'POST':
        try:
            user_id = session.get("id")
            expert_id = request.form["expert_id"]
            remarks = request.form["remarks"]

            method = COMPREHENSIVE
            file = request.files['file']

            if expert_id is None:
                expert_id = 0

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        if file is not None:
            filename = file.filename
            filepath = services_container.file_handler.upload_single(file, "comprehensive")
            return services_container.user_handler.comprehensive_handler(user_id, remarks, method, filepath, filename,
                                                                         expert_id)
        else:
            return response('上传失败', 1001, {})


@user.route('/new_market', methods=['POST', 'GET'])
@permission_required(USER)
def new_market():
    # TEMP 在生产环境中将被弃用
    if request.method == 'GET':
        print(services_container)
        print(services_container.i)
        return render_template("new_comprehensive.html")

    if request.method == 'POST':
        try:
            user_id = session.get("id")
            # expert_id = request.form["expert_id"]
            # remarks = request.form["remarks"]
            expert_id = request.form.get("expert_id")
            remarks = request.form.get("remarks")

            method = MARKET
            file = request.files['file']

            if expert_id is None:
                expert_id = 0

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        if file is not None:
            filename = file.filename
            filepath = services_container.file_handler.upload_single(file, "market")
            return services_container.user_handler.market_handler(user_id, remarks, method, filepath, filename,
                                                                  expert_id)
        else:
            return response('上传失败', 1001, {})


# 查看工单详情
@user.route('/detail_work_order', methods=['GET', 'POST'])
@permission_required(USER)
def work_order_detail():
    if request.method == 'GET':
        return render_template("detail.html")

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                order_id = data.get('order_id')

            else:
                order_id = request.form.get('order_id')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return services_container.data_handler.get_work_order_detail_by_id(order_id)


# 查看所有工单
@user.route('/all_work_order', methods=['GET'])
@permission_required(USER)
def work_order_all():
    return response_multiple("查询成功", 200, dao_service.work_order_dao.getByUserId(session.get('id')))


@user.route('/get_work_order', methods=['GET', 'POST'])
@permission_required(USER)
def get_work_order():
    if request.method == 'GET':
        # return response_multiple("查询成功", 200, dao_service.work_order_dao.getAll())
        return render_template("get.html")

    if request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                order_id = data.get('order_id')
                status = data.get('status')
                page = data.get('page')
                per_page = data.get('per_page')

            else:
                order_id = request.form.get('order_id')
                status = request.form.get('status')
                page = request.form.get('page')
                per_page = request.form.get('per_page')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return response_dict("查询成功", 200,
                             dao_service.work_order_dao.getFuzzy(user_id=session.get("id"), order_id=order_id,
                                                                 status=status,
                                                                 page=page, per_page=per_page))


@user.route('/get_log', methods=['GET', 'POST'])
@permission_required(USER)
def get_log():
    if request.method == 'GET':
        return response_dict("查询成功", 200,
                             dao_service.log_dao.getByUser(user_id=session.get("id")))
    elif request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                page = data.get('page')
                per_page = data.get('per_page')

            else:
                page = request.form.get('page')
                per_page = request.form.get('per_page')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return response_dict("查询成功", 200,
                             dao_service.work_order_dao.getFuzzy(user_id=session.get("id"),page=page, per_page=per_page))


@user.route('/apply_for_expert', methods=['GET', 'POST'])
@permission_required(USER)
def apply_for_expert():
    if request.method == 'GET':
        return render_template("apply.html")
    elif request.method == 'POST':
        try:
            data = request.get_json(silent=True)

            if data is not None:
                realname = data.get('realname')
                job_title = data.get('job_title')
                introduction = data.get('introduction')

            else:
                realname = request.form.get('realname')
                job_title = request.form.get('job_title')
                introduction = request.form.get('introduction')

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        return services_container.user_handler.apply_for_expert(realname, job_title, introduction)

# @user.route('/get_all_user', methods=['GET'])
# @permission_required(USER)
# def get_all_user():
#     return response_multiple("所有人员返回成功", 200, dao_service.user_info_dao.getAll())
#
#
# @user.route('/get_all_expert', methods=['GET'])
# @permission_required(USER)
# def get_all_expert():
#     return response_multiple("所有人员返回成功", 200, dao_service.expert_info_dao.getAll())


'''
          
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
