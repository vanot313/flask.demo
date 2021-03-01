from dao.admin_info import AdminInfoDao
from dao.comprehensive_valuation import ComprehensiveValuationDao
from dao.cost_valuation import CostValuationDao
from dao.earning_valuation import EarningValuationDao
from dao.expert_apply import ExpertApplyDao
from dao.expert_info import ExpertInfoDao
from dao.log import LogDao
from dao.login import LoginDao
from dao.login_log import LoginLogDao
# from dao.market_approach import
from dao.role import RoleDao
from dao.user import UserDao
from dao.user_info import UserInfoDao
from dao.user_role import UserRoleDao
from dao.work_order import WorkOrderDao


class DaoService:
    admin_info_dao = AdminInfoDao()
    comprehensive_valuation_dao = ComprehensiveValuationDao()
    cost_valuation_dao = CostValuationDao()
    earning_valuation_dao = EarningValuationDao()
    expert_apply_dao = ExpertApplyDao()
    expert_info_dao = ExpertInfoDao()
    log_dao = LogDao()
    login_dao = LoginDao()
    login_log_dao = LoginLogDao()
    role_dao = RoleDao()
    user_dao = UserDao()
    user_info_dao = UserInfoDao()
    user_role_dao = UserRoleDao()
    work_order_dao = WorkOrderDao()





