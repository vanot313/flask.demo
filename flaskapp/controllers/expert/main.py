from flask import *
from services import *
from util.response import *
from util.permission import *
from common.models import *
from dao import dao_service
from application import app
from config.macro_setting import *

# 创建一个蓝图对象
from util.response import response

expert = Blueprint("expert", __name__)


@expert.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if services_container.login_handler.is_login():
            return redirect(url_for('expert.detail'))
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

        return services_container.login_handler.login_expert(username, password)


# 登出 注销 session
@expert.route('/logout', methods=['GET'])
@permission_required(EXPERT)
def logout():
    return services_container.login_handler.logout()


@expert.route("/detail", methods=['GET'])
@permission_required(EXPERT)
def detail():
    return response("success", 200, dao_service.expert_info_dao.getById(session.get('id')).first())


# 修改个人信息
@expert.route('/update', methods=['GET', 'POST'])
@permission_required(EXPERT)
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

        return services_container.expert_handler.update_info(email, mobile, location, birth, description)


# 查看所有待评估工单
@expert.route('/all_wait_work_order', methods=['POST', 'GET'])
@permission_required(EXPERT)
def all_wait_work_order():
    if request.method == 'GET':
        return render_template('get.html')
    else:
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

        return response_dict("查询成功", 200, dao_service.work_order_dao.getFuzzy(status=ORDER_WAIT, no_method=4, page=page,
                                                                              per_page=per_page))


# 查看自己负责的工单
@expert.route('/all_self_work_order', methods=['POST'])
@permission_required(EXPERT)
def all_self_work_order():
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

    return response_dict("查询成功", 200, dao_service.work_order_dao.getFuzzy(expert_id=session.get('id'), page=page, per_page=per_page))


@expert.route("/detail_work_order", methods=['GET', 'POST'])
@permission_required(EXPERT)
def detail_work_order():
    if request.method == 'GET':
        return render_template("detail.html")
    else:
        try:
            data = request.get_json(silent=True)

            if data is not None:
                order_id = data.get('order_id')
            else:
                order_id = request.form.get("order_id")

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        # TODO 切换回受保护的查询 get_work_order_detail_by_id
        return services_container.data_handler.get_work_order_detail_by_id_grant(order_id)


@expert.route('/download_order_file', methods=['POST', 'GET'])
@permission_required(EXPERT)
def download_order_file():
    if request.method == 'GET':
        return render_template("get.html")
    else:
        try:
            data = request.get_json(silent=True)

            if data is not None:
                order_id = data.get('order_id')
            else:
                order_id = request.form.get("order_id")

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        filepath = dao_service.work_order_dao.getByOrderId(order_id).first().file_path

        return services_container.file_handler.download_file(filepath=filepath)


@expert.route("/process_comprehensive", methods=['GET', 'POST'])
@permission_required(EXPERT)
def process_comprehensive():
    if request.method == 'GET':

        pass
    else:
        try:
            data = request.get_json(silent=True)
            if data is not None:
                order_id = data.get('order_id')

                rareness = data.get('rareness')
                timeliness = data.get('timeliness')
                dimensional = data.get('dimensional')
                economy = data.get('economy')

                quality_weight = data.get('quality_weight')
                applied_weight = data.get('applied_weight')


            else:
                order_id = request.form.get("order_id")

                rareness = request.form.get("rareness")
                timeliness = request.form.get("timeliness")
                dimensional = request.form.get("dimensional")
                economy = request.form.get("economy")

                quality_weight = request.form.get("quality_weight")
                applied_weight = request.form.get("applied_weight")
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        rareness = float(rareness)
        timeliness = float(timeliness)
        dimensional = float(dimensional)
        economy = float(economy)
        for i in range(0, 5):
            quality_weight[i] = float(quality_weight[i])
        for i in range(0, 5):
            applied_weight[i] = float(applied_weight[i])

        return services_container.expert_handler.comprehensive_handler(order_id, rareness, timeliness, dimensional,
                                                                       economy, quality_weight, applied_weight)


@expert.route("/process_cost", methods=['GET', 'POST'])
@permission_required(EXPERT)
def process_cost():
    if request.method == 'GET':
        return render_template("cost.html")
    else:
        try:

            data = request.get_json(silent=True)
            if data is not None:
                order_id = data.get('order_id')

                R = data.get('R')
                C = data.get('C')
                II = data.get('II')
                M = data.get('M')
                E = data.get('E')

            else:
                order_id = request.form.get('order_id')

                R = request.form.get("R")
                C = request.form.get("C")
                II = request.form.get("II")
                M = request.form.get("M")
                E = request.form.get("E")

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        R = float(R)
        C = float(C)
        II = float(II)
        M = float(M)
        E = float(E)

        return services_container.expert_handler.cost_handler(order_id, R, C, II, M, E)


@expert.route("/process_earning", methods=['GET', 'POST'])
@permission_required(EXPERT)
def process_earning():
    if request.method == 'GET':
        # TODO 返回给专家用户指定的公司名称/数据集名称
        pass
    else:
        try:
            data = request.get_json(silent=True)

            if data is not None:
                order_id = data.get('order_id')

                r = data.get('r')
                n = data.get('n')
                R = data.get('RI')


            else:
                order_id = request.form.get("order_id")

                n = request.form.get("n")
                r = request.form.get("r")
                R = request.form.get("RI")

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据接收异常", 1002, {})

        n = int(n)
        r = float(r)
        for i in range(0, n):
            R[i] = float(R[i])

        return services_container.expert_handler.earning_handler(order_id, n, r, R)


# PROBLEM
# 代码存在大量冗余，每次接收数据的函数都被相似的函数结构包裹
