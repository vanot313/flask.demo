from flask import session

from algorithm.comprehensive_valuation import ComprehensiveValuationA
from algorithm.cost_valuation import CostValuationA
from algorithm.earning_valuation import EarningValuationA
from common.models import *
from dao import dao_service

from application import *
from util.response import *


class UserHandler:
    def market_handler(self, user_id, remarks, method, filepath, filename, expert_id):
        if expert_id != 0:
            expert_name = dao_service.expert_info_dao.getById(expert_id).first().username
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method, file_path=filepath,
                                       file_name=filename, expert_id=expert_id, expert_name=expert_name)
            dao_service.work_order_dao.add(new_work_order)
        elif expert_id == 0:
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method, file_path=filepath,
                                       file_name=filename, expert_id=expert_id)
            dao_service.work_order_dao.add(new_work_order)
        else:
            return response('创建失败', 1002, {})

        # order_id = new_work_order.order_id
        # new_comprehensive = ComprehensiveValuation(order_id=order_id)
        # dao_service.comprehensive_valuation_dao.add(new_comprehensive)

        # c = ComprehensiveValuationA()
        # c.quality_value('../uploadfile/' + filepath)
        # c.applied_value(0.8, 0.2, 0.5, 0.5)
        # c.matrix_value([1, 3, 5, 3, 5, 3], [3, 5, 9, 3, 3, 3])
        # c.calculate()
        # print(c.S)

        result = {'msg': "工单申请成功", 'code': 200,  'data': serialize(new_work_order),
                  'success': 'true'}
        return jsonify(result)

    def comprehensive_handler(self, user_id, remarks, method, filepath, filename, expert_id):
        if expert_id != 0:
            expert_name = dao_service.expert_info_dao.getById(expert_id).first().username
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method, file_path=filepath,
                                       file_name=filename, expert_id=expert_id, expert_name=expert_name)
            dao_service.work_order_dao.add(new_work_order)
        elif expert_id == 0:
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method, file_path=filepath,
                                       file_name=filename, expert_id=expert_id)
            dao_service.work_order_dao.add(new_work_order)
        else:
            return response('创建失败', 1002, {})

        order_id = new_work_order.order_id
        new_comprehensive = ComprehensiveValuation(order_id=order_id)
        dao_service.comprehensive_valuation_dao.add(new_comprehensive)

        result = {'msg': "工单申请成功", 'code': 200, 'data': serialize(new_work_order),
                  'success': 'true'}
        return jsonify(result)

    def cost_handler(self, user_id, remarks, method, expert_id):
        if expert_id != 0:
            expert_name = dao_service.expert_info_dao.getById(expert_id).first().username
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method,
                                       expert_id=expert_id, expert_name=expert_name)
            dao_service.work_order_dao.add(new_work_order)
        elif expert_id == 0:
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method,
                                       expert_id=expert_id)
            dao_service.work_order_dao.add(new_work_order)
        else:
            return response('创建失败', 1002, {})

        order_id = new_work_order.order_id
        new_cost = CostValuation(order_id=order_id)
        dao_service.cost_valuation_dao.add(new_cost)

        result = {'msg': "工单申请成功", 'code': 200, 'data': serialize(new_work_order),
                  'success': 'true'}
        return jsonify(result)

    def earning_handler(self, user_id, remarks, method, expert_id):
        if expert_id != 0:
            expert_name = dao_service.expert_info_dao.getById(expert_id).first().username
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method,
                                       expert_id=expert_id, expert_name=expert_name)
            dao_service.work_order_dao.add(new_work_order)
        elif expert_id == 0:
            new_work_order = WorkOrder(user_id=user_id, u_remarks=remarks, method=method,
                                       expert_id=expert_id)
            dao_service.work_order_dao.add(new_work_order)
        else:
            return response('创建失败', 1002, {})

        order_id = new_work_order.order_id
        new_earning = EarningValuation(order_id=order_id)
        dao_service.earning_valuation_dao.add(new_earning)

        result = {'msg': "工单申请成功", 'code': 200, 'data': serialize(new_work_order),
                  'success': 'true'}
        return jsonify(result)

    def update_info(self, email, mobile, location, birth, description):
        try:
            target = dao_service.user_info_dao.getById(session.get('id')).first()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        if email is not None:
            target.email = email

        if mobile is not None:
            target.mobile = mobile

        if location is not None:
            target.location = location

        if birth is not None:
            target.birth = birth

        if description is not None:
            target.description = description

        try:
            resp = dao_service.user_info_dao.update(target)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("修改成功", 200, resp)

    def get_all_user(self):
        try:
            return response_multiple("所有人员返回成功", 200, dao_service.user_info_dao.getAll())
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

    def get_all_expert(self):
        try:
            return response_multiple("所有人员返回成功", 200, dao_service.expert_info_dao.getAll())
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})
