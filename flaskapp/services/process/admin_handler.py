from flask import session

from common.models import *
from dao import dao_service
from config.macro_setting import *

from application import db, app
from util.response import response


class AdminHandler:
    def update_info(self, email, mobile, location, birth, description):
        try:
            target = dao_service.admin_info_dao.getById(session.get('id')).first()
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
            resp = dao_service.admin_info_dao.update(target)
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("失败", 1001, {})

        return response("修改成功", 200, resp)

    def update_user_info(self, id, email, mobile, location, birth, description):
        try:
            target = dao_service.user_info_dao.getById(id).first()
        except Exception as e:
            app.logger.info('Exception: %s', e)
            return response("查询用户信息失败", 1001, {})

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
            return response("修正信息失败", 1001, {})

        return response("修改成功", 200, resp)

    def update_expert_apply(self, status, apply_id):

        try:
            apply = dao_service.expert_apply_dao.getByApplyId(apply_id).first()
            apply.status = status
            # db.session.close()

            dao_service.expert_apply_dao.update(apply)
            user_id = apply.user_id

            if int(status) == PASS:
                new_userrole = UserRole(user_id=user_id, role_id=EXPERT)
                dao_service.user_role_dao.add(new_userrole)

                new_log = Log(from_id=session.get('id'), to_id=user_id, operation="允许专家权限")
                dao_service.log_dao.add(new_log)

            else:
                new_log = Log(from_id=session.get('id'), to_id=user_id, operation="拒绝专家权限")
                dao_service.log_dao.add(new_log)

        except:
            return response("数据库操作失败", 1001, {})

        return response("申请处理成功", 200, apply)
