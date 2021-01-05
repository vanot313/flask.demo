# coding:utf-8
from application import app
from controllers.index import data
from controllers.uploader import uploader
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器和错误处理
from interceptors.Auth import *
from interceptors.errorHandler import *

# 注册蓝图blueprint对象
app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(uploader, url_prefix="/uploader")

