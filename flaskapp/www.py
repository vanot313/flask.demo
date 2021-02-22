# coding:utf-8
from application import app
from controllers.data import data
from controllers.uploader import uploader
from controllers.testpage import testpage
from controllers.main import main
#admin
from controllers.dataCollector.index import dataCollector

#user
from controllers.user.login.index import user_login

from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器和错误处理
from interceptors.errorHandler import *

# 注册蓝图 blueprint 对象
app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(uploader, url_prefix="/uploader")
app.register_blueprint(testpage, url_prefix="/test")
app.register_blueprint(main, url_prefix="/main")

#用户管理接口
app.register_blueprint(user_login, url_prefix="/user/login")


#管理员接口
app.register_blueprint(dataCollector, url_prefix="/collector")
