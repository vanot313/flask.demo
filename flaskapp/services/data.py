from flask import *
from application import app
from common.models import *
from dao import dao_service
from config.method_setting import *
from util.response import *


class DataHandler:
    def __init__(self):
        pass

    def get_work_order_detail_by_id(self, order_id):
        tuple = []

        base = dao_service.work_order_dao.getByOrderId(order_id).first()

        if base.user_id == session.get('id'):
            tuple.append(base)

            if int(base.method) == int(COST):
                detail = dao_service.cost_valuation_dao.getByOrderId(order_id).first()
                tuple.append(detail)

            if int(base.method) == int(COMPREHENSIVE):
                detail = dao_service.comprehensive_valuation_dao.getByOrderId(order_id).first()
                tuple.append(detail)

            if int(base.method) == int(EARNING):
                detail = dao_service.earning_valuation_dao.getByOrderId(order_id).first()
                tuple.append(detail)

            return response_multiple("查询成功", 200, tuple)

        else:
            return response("无访问权限", 302, {})