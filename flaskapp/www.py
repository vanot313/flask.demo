# coding:utf-8
from application import app
from controllers.data import data
from controllers.uploader import uploader
from controllers.testpage import testpage


from controllers.admin.main import admin
from controllers.expert.main import expert

#admin
from controllers.dataCollector.index import dataCollector

#user
from controllers.user.base.index import user

from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器和错误处理
from interceptors.errorHandler import *

# 注册蓝图 blueprint 对象


app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(uploader, url_prefix="/uploader")
app.register_blueprint(testpage, url_prefix="/test")

# 管理员接口
app.register_blueprint(admin, url_prefix="/admin")

# 专家接口
app.register_blueprint(expert, url_prefix="/expert")

# 用户管理接口
app.register_blueprint(user, url_prefix="/user")

# 数据爬取器接口
app.register_blueprint(dataCollector, url_prefix="/collector")
