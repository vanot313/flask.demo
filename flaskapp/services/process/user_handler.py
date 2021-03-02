from common.models import *
from dao import dao_service

from application import db
from util.response import response


class UserHandler:
    def ComprehensiveHandler(self, user_id, remarks, method, filename):
        new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method, file_name=filename)
        dao_service.work_order_dao.add(new_work_order)

        order_id = new_work_order.order_id
        new_comprehensive = ComprehensiveValuation(order_id=order_id)
        dao_service.comprehensive_valuation_dao.add(new_comprehensive)

        return response("工单申请成功", 200, new_work_order)

    def CostHandler(self, user_id, remarks, method):
        new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method)
        dao_service.work_order_dao.add(new_work_order)

        order_id = new_work_order.order_id
        new_cost = CostValuation(order_id=order_id)
        dao_service.cost_valuation_dao.add(new_cost)

        return response("工单申请成功", 200, new_work_order)

    def EarningHandler(self, user_id, remarks, method):
        new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method)
        dao_service.work_order_dao.add(new_work_order)

        order_id = new_work_order.order_id
        new_earning = EarningValuation(order_id=order_id)
        dao_service.earning_valuation_dao.add(new_earning)

        return response("工单申请成功", 200, new_work_order)
