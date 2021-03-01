# coding:utf-8
from flask import *
from application import db
from common.models.user import User
import random
from util import str_tools, response
import subprocess
import os

dataCollector = Blueprint("dataCollector", __name__)


# 上传代码
@dataCollector.route("/upload", methods=['POST'])
def upload():
    filename = request.form.get('name')
    file = request.files('file')

    # 保存路径
    file.save(filename)

    return response.response("upload success", 200, {})


# 执行爬虫
@dataCollector.route("/execute", methods=['POST'])
def execute():
    status = 1
    output = "nothing"

    exeFile = request.form.get('exeFile')
    outFile = request.form.get('outFile')

    # 判断是否存在爬虫文件夹
    if not os.path.exists("webScrapy"):
        status, output = subprocess.getstatusoutput('scrapy startproject webScrapy')
        if status == 1:
            return response.response("爬虫框架创建失败", 200, {"status": status,
                                                       "output": output})

    cmd = 'cd ./webScrapy/webScrapy/spiders/ & scrapy crawl ' + exeFile + ' -o ' + outFile
    status, output = subprocess.getstatusoutput(cmd)

    # 返回参数
    # status 是否完成爬虫 1表示失败 0表示成功
    # output 爬虫完成的命令行信息 失败时返回
    if status == 1:
        return response.response("爬虫失败", 200, {"status": status,
                                               "output": output})
    else:
        return response.response("爬虫成功", 200, {"status": status})


# index
@dataCollector.route("/", methods=['GET'])
def index():
    return response.response("爬虫", 200, 'hello')
