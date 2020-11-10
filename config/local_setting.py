#本地开发配置文件
from config.base_setting import *
#这样的话就可以覆盖配置了
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Ji1234@101.132.131.184/mytest"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENCODING = "utf-8"
SECRET_KEY = None