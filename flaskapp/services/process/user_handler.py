from services.algorithm.comprehensive_valuation import *
from services.algorithm.cost_valuation import *
from services.algorithm.earning_valuation import *
from common.models.work_order import WorkOrder
from common.models.comprehensive_valuation import ComprehensiveValuation
from common.models.cost_valuation import CostValuation
from common.models.work_order import WorkOrder
from common.models.earning_valuation import EarningValuation

from application import db
from util.response import response


def UserComprehensiveHandler(user_id, remarks, method, filename):
    new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method, file_name=filename)
    db.session.add(new_work_order)
    db.session.commit()

    order_id = new_work_order.order_id
    new_comprehensive = ComprehensiveValuation(order_id=order_id)
    db.session.add(new_comprehensive)
    db.session.commit()

    return response("工单申请成功", 200, new_work_order)


def UserCostHandler(user_id, remarks, method):
    new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method)
    db.session.add(new_work_order)
    db.session.commit()

    order_id = new_work_order.order_id
    new_cost = CostValuation(order_id=order_id)
    db.session.add(new_cost)
    db.session.commit()

    return response("工单申请成功", 200, new_work_order)


def UserEarningHandler(user_id, remarks, method):
    new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method)
    db.session.add(new_work_order)
    db.session.commit()

    order_id = new_work_order.order_id
    new_earning = EarningValuation(order_id=order_id)
    db.session.add(new_earning)
    db.session.commit()

    return response("工单申请成功", 200, new_work_order)