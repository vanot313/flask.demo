from functools import wraps
from flask import session, abort
from dao import *


def permission_can(current_user_role, permission):
    """
    检测用户是否有特定权限
    :param current_user_role
    :param permission
    :return:
    """
    return current_user_role == permission


def permission_required(permission):
    """
    权限认证装饰器
    :param permission:
    :return:
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                print("session:", session.get('id'))
                current_user_role = dao_service.user_role_dao.getById(session.get('id'))

                if not current_user_role:
                    abort(403)

                for role in current_user_role:

                    if permission_can(role.role_id, permission):
                        return f(*args, **kwargs)

                abort(403)
            except Exception as e:
                print(e)
                abort(403)

        return decorated_function

    return decorator
