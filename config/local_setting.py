#本地开发配置文件
from config.base_setting import *
#这样的话就可以覆盖配置了
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:XXXXXXXXXX@XXX.XXX.XXX.XXX/mytest"
SECRET_KEY = "12345IT1995"