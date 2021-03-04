# coding:utf-8
from application import app

from controllers.admin.main import admin
from controllers.expert.main import expert
from controllers.user.main import user

# admin
from controllers.dataCollector.index import dataCollector

from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器和错误处理
from interceptors.errorHandler import *

# 注册蓝图 blueprint 对象

# 管理员接口
app.register_blueprint(admin, url_prefix="/admin")

# 专家接口
app.register_blueprint(expert, url_prefix="/expert")

# 用户管理接口
app.register_blueprint(user, url_prefix="/user")

# 数据爬取器接口
app.register_blueprint(dataCollector, url_prefix="/collector")
