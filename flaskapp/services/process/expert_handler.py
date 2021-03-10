# coding:utf-8
from flask import session

from common.models import *
from dao import *
from services import services_container
from algorithm.cost_valuation import CostValuationA
from algorithm.earning_valuation import EarningValuationA
from algorithm.comprehensive_valuation import *
from config.macro_setting import *


from application import *
from util.response import *

from services.file import FileHandler


class ExpertHandler:
    def comprehensive_handler(self, work_order_id, rareness, timeness, dimensional, economy, quality_weight,
                              applied_weight):
        handler = ComprehensiveValuation()

        # TODO 得到数据集文件安置的解决方案
        address = ""

        if handler.quality_value(address) == FILE_ERROR:
            response("文件错误", 1001, {})

        if handler.applied_value(rareness, timeness, dimensional, economy) == Q_ERROR:
            response("质量对比矩阵未通过一致性检验，需对对比矩阵重新构造", 1001, {})
        elif handler.applied_value(rareness, timeness, dimensional, economy) == A_ERROR:
            response("应用对比矩阵未通过一致性检验，需对对比矩阵重新构造", 1001, {})

        handler.matrix_value(quality_weight[0], quality_weight[1],
                             quality_weight[2], quality_weight[3],
                             quality_weight[4], quality_weight[5],
                             applied_weight[0], applied_weight[1],
                             applied_weight[2], applied_weight[3],
                             applied_weight[4], applied_weight[5])

        handler.calculate()

        # TODO 将估值数据存入数据库

        # TODO 并返回结果

        return 1

    def cost_handler(self, work_order_id, R, C, II, M, E):

        handler = CostValuationA()
        handler.getpar(R, C, II, M, E)
        handler.calculate()

        try:
            order_detail = dao_service.cost_valuation_dao.getByOrderId(work_order_id).first()
            order_detail.P = handler.P
            order_detail.R = handler.R
            order_detail.C = handler.C
            order_detail.II = handler.II
            order_detail.M = handler.M
            order_detail.E = handler.E

            dao_service.cost_valuation_dao.update(order_detail)

            order = dao_service.work_order_dao.getByOrderId(work_order_id).first()
            order.status = ORDER_DONE
            dao_service.work_order_dao.update(order)

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("提交成功", 200, order_detail)

    def earning_handler(self, work_order_id, n, r, R):
        handler = EarningValuationA()
        handler.getpar(n, r, R)
        handler.calculate()

        try:
            order_detail = dao_service.earning_valuation_dao.getByOrderId(work_order_id).first()
            order_detail.n = handler.n
            order_detail.r = handler.r
            order_detail.RI = handler.R

            dao_service.cost_valuation_dao.update(order_detail)

            order = dao_service.work_order_dao.getByOrderId(work_order_id).first()
            order.status = ORDER_DONE
            dao_service.work_order_dao.update(order)

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("算法进行失败", 1001, {})

        return response("提交成功", 200, order_detail)

    def update_info(self, email, mobile, location, birth, description):
        try:
            target = dao_service.expert_info_dao.getById(session.get('id')).first()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据库查询失败", 1001, {})

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
            resp = dao_service.expert_info_dao.update(target)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("修改成功", 200, resp)

