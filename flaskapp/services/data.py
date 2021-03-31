from flask import *
from application import app
from common.models import *
from dao import dao_service
from config.macro_setting import *
from util.response import *


class DataHandler:
    def __init__(self):
        pass

    def get_work_order_detail_by_id(self, order_id):
        tuple = {}

        try:
            base = dao_service.work_order_dao.getByOrderId(order_id).first()

            if base.user_id != session.get('id'):
                # tuple.append(base)
                tuple['base'] = base

                if int(base.method) == int(COST):
                    detail = dao_service.cost_valuation_dao.getByOrderId(order_id).first()
                    # tuple.append(detail)
                    tuple['detail'] = detail

                if int(base.method) == int(COMPREHENSIVE):
                    detail = dao_service.comprehensive_valuation_dao.getByOrderId(order_id).first()
                    # tuple.append(detail)
                    tuple['detail'] = detail

                if int(base.method) == int(EARNING):
                    detail = dao_service.earning_valuation_dao.getByOrderId(order_id).first()
                    # tuple.append(detail)
                    tuple['detail'] = detail
                result = {'msg': "工单查询成功", 'code': 200,
                          'data': {'base': serialize(tuple['base']), 'detail': serialize(tuple['detail'])},
                          'success': 'true'}
                return jsonify(result)
            else:
                return response("无访问权限", 302, {})

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

    def get_work_order_detail_by_id_grant(self, order_id):
        tuple = {}

        try:
            base = dao_service.work_order_dao.getByOrderId(order_id).first()

            # tuple.append(base)
            tuple['base'] = base

            if int(base.method) == int(COST):
                detail = dao_service.cost_valuation_dao.getByOrderId(order_id).first()
                # tuple.append(detail)
                tuple['detail'] = detail

            if int(base.method) == int(COMPREHENSIVE):
                detail = dao_service.comprehensive_valuation_dao.getByOrderId(order_id).first()
                # tuple.append(detail)
                tuple['detail'] = detail

            if int(base.method) == int(EARNING):
                detail = dao_service.earning_valuation_dao.getByOrderId(order_id).first()
                # tuple.append(detail)
                tuple['detail'] = detail
            result = {'msg': "工单申请成功", 'code': 200,
                      'data': {'base': serialize(tuple['base']), 'detail': serialize(tuple['detail'])},
                      'success': 'true'}
            return jsonify(result)

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

    def get_work_order_info_by_id(self, order_id):
        try:
            base = dao_service.work_order_dao.getByOrderId(order_id)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})
        return response_multiple("查询成功", 200, base)
