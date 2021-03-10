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
            return dao_service.expert_info_dao.getById(session.get('id')).first()

        return render_template("login.html")
    else:
        # username = request.form.get('name')
        # password = request.form.get('password')

        data = request.get_json(silent=True)

        username = data['username']
        password = data['password']

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
@expert.route('/update', methods=['POST', 'GET'])
@permission_required(EXPERT)
def update():
    if request.method == 'GET':
        return render_template("update.html")

    if request.method == 'POST':
        # email = request.form.get('email')
        # mobile = request.form.get('mobile')
        # location = request.form.get('location')
        # birth = request.form.get('birth')
        # description = request.form.get('description')

        data = request.get_json(silent=True)

        birth = data['birth']
        location = data['location']
        description = data['description']
        email = data['email']
        mobile = data['mobile']

        return services_container.expert_handler.update_info(email, mobile, location, birth, description)


# 查看所有待评估工单
@expert.route('/all_wait_work_order', methods=['GET'])
@permission_required(EXPERT)
def all_wait_work_order():
    return response_multiple("查询成功", 200, dao_service.work_order_dao.getFit(status=ORDER_WAIT))


# 查看自己负责的工单
@expert.route('/all_self_work_order', methods=['GET'])
@permission_required(EXPERT)
def all_self_work_order():
    return response_multiple("查询成功", 200, dao_service.work_order_dao.getFit(expert_id=session.get('id')))


@expert.route("/detail_work_order", methods=['GET', 'POST'])
@permission_required(EXPERT)
def detail_work_order():
    if request.method == 'GET':
        return render_template("getorderid.html")
    else:
        # order_id = request.form.get("order_id")

        data = request.get_json(silent=True)

        order_id = data['order_id']

        return services_container.data_handler.get_work_order_info_by_id(order_id)


@expert.route('/download_order_file', methods=['POST', 'GET'])
@permission_required(EXPERT)
def download_order_file():
    if request.method == 'GET':
        return render_template("getorderid.html")
    else:
        # order_id = request.form.get("order_id")

        data = request.get_json(silent=True)

        order_id = data['order_id']

        filename = dao_service.work_order_dao.getByOrderId(order_id).first().file_name

        return services_container.file_handler.download_file(filename=filename)


@expert.route("/process_comprehensive", methods=['GET', 'POST'])
@permission_required(EXPERT)
def process_comprehensive():
    if request.method == 'GET':
        # TODO 返回给专家用户上传的数据集

        pass
    else:
        # order_id = request.form.get("order_id")
        #
        # rareness = request.form.get("rareness")
        # timeliness = request.form.get("timeliness")
        # dimensional = request.form.get("dimensional")
        # economy = request.form.get("economy")
        #
        # quality_weight = json.loads(request.form.get("quality_weight"))
        # applied_weight = json.loads(request.form.get("applied_weight"))

        data = request.get_json(silent=True)

        order_id = data['order_id']

        rareness = data['rareness']
        timeliness = data['timeliness']
        dimensional = data['dimensional']
        economy = data['economy']

        quality_weight = json.loads(data['quality_weight'])
        applied_weight = json.loads(data['applied_weight'])

        return services_container.expert_handler.comprehensive_handler(order_id, rareness, timeliness, dimensional,
                                                                       economy, quality_weight, applied_weight)


@expert.route("/process_cost", methods=['GET', 'POST'])
@permission_required(EXPERT)
def process_cost():
    if request.method == 'GET':
        return render_template("cost.html")
    else:
        # order_id = request.form.get("order_id")
        #
        # R = request.form.get("R")
        # C = request.form.get("C")
        # II = request.form.get("II")
        # M = request.form.get("M")
        # E = request.form.get("E")

        data = request.get_json(silent=True)

        order_id = data['order_id']

        R = data['R']
        C = data['C']
        II = data['II']
        M = data['M']
        E = data['E']

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
        data = request.get_json(silent=True)

        if data is not None:
            order_id = data['order_id']

            r = data['r']
            n = data['n']
            R = json.loads(data['R'])

        else:
            order_id = request.form.get("order_id")

            n = request.form.get("n")
            r = request.form.get("r")
            R = json.loads(request.form.get("R"))

            n = int(n)
            r = float(r)
            for i in range(1, n + 1):
                R[i] = float(R[i])

        return services_container.expert_handler.earning_handler(order_id, n, r, R)


@expert.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return session.get('id')
