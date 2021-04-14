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
        handler = ComprehensiveValuationA()

        # 读取目标数据集位置
        try:
            order = dao_service.work_order_dao.getByOrderId(work_order_id).first()
        except:
            return response("数据库查询失败", 1001, {})

        file_path = order.file_path
        address = os.path.join('uploadfile', file_path)

        # 算法处理片段
        msg = SUCCESS

        msg = handler.quality_value(address)

        if msg == FILE_ERROR:
            return response("文件错误", 1001, {})

        msg = handler.applied_value(rareness, timeness, dimensional, economy)

        msg = handler.matrix_value(quality_weight, applied_weight)
        if msg == Q_ERROR:
            return response("质量对比矩阵未通过一致性检验，需对对比矩阵重新构造", 1001, {})
        elif msg == A_ERROR:
            return response("应用对比矩阵未通过一致性检验，需对对比矩阵重新构造", 1001, {})
        handler.calculate()

        # 数据库保存模型片段
        try:
            order_detail = dao_service.comprehensive_valuation_dao.getByOrderId(work_order_id).first()
            order_detail.full = handler.full
            order_detail.correct = handler.correct
            order_detail.uniformity = handler.uniformity
            order_detail.repeatability = handler.repeat
            order_detail.rareness = handler.rareness
            order_detail.timeliness = handler.timeliness
            order_detail.dimensional = handler.dimensional
            order_detail.economy = handler.economy
            order_detail.quality_weight = str(handler.quality_weight.tolist())
            order_detail.applied_weight = str(handler.applied_weight.tolist())
            order_detail.RI = str(handler.RI)
            order_detail.Sq = float(handler.Sq.real)
            order_detail.Sa = float(handler.Sa.real)
            order_detail.S = float(handler.S.real)

            dao_service.comprehensive_valuation_dao.update(order_detail)

            order.expert_id = session.get('id')
            order.status = ORDER_DONE
            dao_service.work_order_dao.update(order)

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据库操作失败", 1001, {})

        new_log = Log(from_id=session.get('id'), to_id=order.user_id, order_id=order.order_id, operation="新建综合估值法工单",
                      username=dao_service.user_info_dao.getById(session.get("id")).first().username)
        dao_service.log_dao.add(new_log)

        return response("提交成功", 200, order_detail)

    def cost_handler(self, work_order_id, R, C, II, M, E):
        handler = CostValuationA()

        # 算法处理片段
        handler.getpar(R, C, II, M, E)
        handler.calculate()

        # 数据库保存模型片段
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
            order.expert_id = session.get('id')
            order.status = ORDER_DONE
            dao_service.work_order_dao.update(order)

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据库操作失败", 1001, {})

        new_log = Log(from_id=session.get('id'), to_id=order.user_id, order_id=order.order_id, operation="评估成本法工单",
                      username=dao_service.user_info_dao.getById(session.get("id")).first().username)
        dao_service.log_dao.add(new_log)

        return response("提交成功", 200, order_detail)

    def earning_handler(self, work_order_id, n, r, R):
        handler = EarningValuationA()

        # 算法处理片段
        handler.getpar(n, r, R)
        handler.calculate()

        # 数据库保存模型片段
        try:
            order_detail = dao_service.earning_valuation_dao.getByOrderId(work_order_id).first()
            order_detail.P = handler.P
            order_detail.n = handler.n
            order_detail.r = handler.r
            order_detail.RI = str(handler.R)

            dao_service.earning_valuation_dao.update(order_detail)
            order = dao_service.work_order_dao.getByOrderId(work_order_id).first()
            order.expert_id = session.get('id')
            order.status = ORDER_DONE
            dao_service.work_order_dao.update(order)

        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("数据库操作失败", 1001, {})

        new_log = Log(from_id=session.get('id'), to_id=order.user_id, order_id=order.order_id, operation="评估收益法工单",
                      username=dao_service.user_info_dao.getById(session.get("id")).first().username)
        dao_service.log_dao.add(new_log)

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
            return response("数据库操作失败", 1001, {})

        new_log = Log(from_id=session.get('id'), to_id=session.get('id'), operation="更新个人信息",
                      username=dao_service.user_info_dao.getById(session.get("id")).first().username)
        dao_service.log_dao.add(new_log)

        return response("修改成功", 200, resp)
