import common.models.user
from flask import *
from services.login import login_user

user_login = Blueprint("user_login", __name__)


@user_login.route("/status", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        return login_user(name, password)