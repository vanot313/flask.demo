import pymysql
from flask import session
from application import app
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from algorithm.comprehensive_valuation import ComprehensiveValuationA
from algorithm.cost_valuation import CostValuationA
from algorithm.earning_valuation import EarningValuationA
from algorithm.market.market_valuation import MarketValuationA
from common.models import *
from config.macro_setting import *
from dao import dao_service

from application import *
from util.response import *


class UserHandler:
    executor = ThreadPoolExecutor(1)

    def market_predict(self, order_id, file_path):

        file_path = os.path.join('uploadfile', file_path)
        handler = MarketValuationA()
        handler.load(file_path)
        handler.predict()

        order_detail = dao_service.market_valutation_dao.getByOrderId(order_id).first()
        order_detail.graininess = float(handler.graininess)
        order_detail.dimension = float(handler.dimension)
        order_detail.activity = float(handler.activity)
        order_detail.scale = float(handler.scale)
        order_detail.correlation = float(handler.correlation)
        order_detail.suggestion = int(handler.suggestion)
        order_detail.amount = float(handler.amount)
        order_detail.size = float(handler.size)
        order_detail.growth = float(handler.growth)
        order_detail.coverage = float(handler.coverage)
        order_detail.attribute = float(handler.attribute)
        order_detail.source = float(handler.source)
        order_detail.maintenance = float(handler.maintenance)
        order_detail.incoming = float(handler.incoming)
        order_detail.outgoing = float(handler.outgoing)

        dao_service.market_valutation_dao.update(order_detail)
        order = dao_service.work_order_dao.getByOrderId(order_id).first()
        order.expert_id = session.get('id')
        order.status = ORDER_DONE
        dao_service.work_order_dao.update(order)



        return response("提交成功", 200, order_detail)

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

        order_id = new_work_order.order_id
        new_comprehensive = MarketValuation(order_id=order_id)
        dao_service.market_valutation_dao.add(new_comprehensive)

        # self.executor.submit(self.market_predict, order_id, filepath)
        self.market_predict(order_id, filepath)

        # order_id = new_work_order.order_id
        # new_comprehensive = ComprehensiveValuation(order_id=order_id)
        # dao_service.comprehensive_valuation_dao.add(new_comprehensive)

        # c = ComprehensiveValuationA()
        # c.quality_value('../uploadfile/' + filepath)
        # c.applied_value(0.8, 0.2, 0.5, 0.5)
        # c.matrix_value([1, 3, 5, 3, 5, 3], [3, 5, 9, 3, 3, 3])
        # c.calculate()
        # print(c.S)

        new_log = Log(from_id=user_id, to_id=user_id, order_id=order_id, operation="新建市场法工单")
        dao_service.log_dao.add(new_log)

        return response("工单申请成功", 200, new_work_order)

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

        new_log = dao_service.log_dao(from_id=user_id, to_id=user_id, order_id=order_id, operation="新建综合估值法工单")
        dao_service.log_dao.add(new_log)

        return response("工单申请成功", 200, new_work_order)

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

        new_log = Log(from_id=user_id, to_id=user_id, order_id=order_id, operation="新建成本法工单")
        dao_service.log_dao.add(new_log)

        return response("工单申请成功", 200, new_work_order)

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

        new_log = Log(from_id=user_id, to_id=user_id, order_id=order_id, operation="新建收益法工单")
        dao_service.log_dao.add(new_log)

        return response("工单申请成功", 200, new_work_order)

    def update_info(self, email, mobile, location, birth, description):
        try:
            target = dao_service.user_info_dao.getById(session.get('id')).first()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        if email is not None and '':
            target.email = email

        if mobile is not None and '':
            target.mobile = mobile

        if location is not None and '':
            target.location = location

        if birth is not None and '':
            target.birth = birth

        if description is not None:
            target.description = description

        try:
            resp = dao_service.user_info_dao.update(target)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        new_log = Log(from_id=session.get('id'), to_id=session.get('id'), operation="更新个人信息")
        dao_service.log_dao.add(new_log)

        return response("修改成功", 200, resp)

    def apply_for_expert(self, realname, job_title, introduction):
        UserInfo = dao_service.user_info_dao.getById(session.get("id")).first()

        try:
            new_apply = ExpertApply(user_id=UserInfo.id, username=UserInfo.username, email=UserInfo.email,
                                    mobile=UserInfo.mobile, realname=realname, job_title=job_title, introduction=introduction)
            dao_service.expert_apply_dao.add(new_apply)
        except:
            return response("数据库插入失败", 1001, {})

        new_log = Log(from_id=session.get('id'), to_id=session.get('id'), operation="申请专家权限")
        dao_service.log_dao.add(new_log)

        return response("申请成功", 200, new_apply)

    # def get_all_user(self):
    #     try:
    #         return response_multiple("所有人员返回成功", 200, dao_service.user_info_dao.getAll())
    #     except Exception as e:
    #         app.logger.info('Exception: %s', e)
    #         return response("失败", 1001, {})
    #
    # def get_all_expert(self):
    #     try:
    #         return response_multiple("所有人员返回成功", 200, dao_service.expert_info_dao.getAll())
    #     except Exception as e:
    #         app.logger.info('Exception: %s', e)
    #         return response("失败", 1001, {})
