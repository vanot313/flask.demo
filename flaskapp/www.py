# coding:utf-8
from application import app
from controllers.data import data
from controllers.uploader import uploader
from controllers.testpage import testpage
from controllers.main import main

from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器和错误处理
from interceptors.Auth import *
from interceptors.errorHandler import *

# 注册蓝图 blueprint 对象
app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(uploader, url_prefix="/uploader")
app.register_blueprint(testpage, url_prefix="/test")
app.register_blueprint(main, url_prefix="/main")

