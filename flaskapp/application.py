# coding:utf-8
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


class Application(Flask):
    def __init__(self, import_name):

        super(Application, self).__init__(import_name)

        self.config.from_pyfile('config/base_setting.py')
        # 暂时不考虑分环境采用config
        self.config.from_pyfile('config/local_setting.py')

        # if "ops_config" in os.environ:
        #     self.config.from_pyfile("config/%s_setting.py" % (os.environ['ops_config']))

        # 将Flaks应用作为参数传入，初始化database
        CORS(self, supports_credentials=True)
        db.init_app(self)

# app = Flask(__name__)
# manager = Manager(app)
#
# app.config.from_pyfile("config/base_setting.py")
# ops_config=local|production
# linux export ops_config=local|production
# windows set ops_config=local|production

# 数据库控制实例
db = SQLAlchemy()
# 生成Flask应用实例 进入__init__初始化实例
app = Application(__name__)
# 脚本控制应用实例
manager = Manager(app)
