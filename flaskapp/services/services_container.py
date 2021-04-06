from dao.crawler import CrawlerDao
from services.process.expert_handler import ExpertHandler
from services.process.user_handler import UserHandler
from services.process.admin_handler import AdminHandler

from services.register import RegisterHandler
from services.login import LoginHandler
from services.file import FileHandler
from services.data import DataHandler


class ServicesContainer:
    i = 1.0

    login_handler = LoginHandler()
    register_handler = RegisterHandler()
    file_handler = FileHandler()

    expert_handler = ExpertHandler()
    user_handler = UserHandler()
    admin_handler = AdminHandler()

    data_handler = DataHandler()

    crawl_handler = CrawlerDao()