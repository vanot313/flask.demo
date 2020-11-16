# coding:utf-8
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        # 暂时不考虑分环境采用config
        self.config.from_pyfile('config/local_setting.py')

        # if "ops_config" in os.environ:
        #     self.config.from_pyfile("config/%s_setting.py" % (os.environ['ops_config']))

        db.init_app(self)


# app = Flask(__name__)
# manager = Manager(app)
#
# app.config.from_pyfile("config/base_setting.py")
# ops_config=local|production
# linux export ops_config=local|production
# windows set ops_config=local|production

db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)
