# coding:utf-8
# 本地开发配置文件
from config.base_setting import *
# 这样的话就可以覆盖配置了
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://administrator:Jiang03.13@49.235.73.129/mytest"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENCODING = "utf-8"
SECRET_KEY = None