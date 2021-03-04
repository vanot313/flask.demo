from services.process.expert_handler import ExpertHandler
from services.process.user_handler import UserHandler

from services.register import RegisterHandler
from services.login import LoginHandler
from services.upload import UploadHandler
from services.data import DataHandler


class ServicesContainer:
    login_handler = LoginHandler()
    register_handler = RegisterHandler()
    upload_handler = UploadHandler()

    expert_handler = ExpertHandler()
    user_handler = UserHandler()

    data_handler = DataHandler()