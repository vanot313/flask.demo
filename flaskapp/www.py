# coding:utf-8
from application import app
from controllers.index import index_page
from controllers.index import first_page
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器和错误处理
from interceptors.Auth import *
from interceptors.errorHandler import *

# 注册蓝图blueprint对象
app.register_blueprint(first_page, url_prefix="/a")
app.register_blueprint(index_page, url_prefix="/")