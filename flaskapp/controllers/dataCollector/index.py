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
    filename = request.form.get('filename')
    remark = request.form.get('remarks')
    file = request.files['file']

    if filename is None:
        return response.response("信息不完全", 1002, {})
    path = './webScrapy/webScrapy/spiders/' + filename
    # 保存路径
    file.save(path)

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
            return jsonify("爬虫框架创建失败", 200, {"status": status,
                                             "output": output})
    if not os.path.exists("collectorFile"):
        os.mkdir('collectorFile')

    if exeFile is None and outFile is None:
        return response.response('请选择文件', 1002, {})

    outFile = '../../../collectorFile/' + outFile
    print(outFile)
    cmd = 'cd ./webScrapy/webScrapy/spiders/ & scrapy crawl ' + exeFile + ' -o ' + outFile
    status, output = 0, ''
    try:
        status, output = subprocess.getstatusoutput(cmd)
    except Exception as e:
        print(e)
        pass

    # 返回参数
    # status 是否完成爬虫 1表示失败 0表示成功
    # output 爬虫完成的命令行信息 失败时返回
    if status == 1:
        return jsonify("爬虫失败", 200, {"status": status,
                                     "output": output})
    else:
        return jsonify("爬虫成功", 200, {"status": status})


@dataCollector.route("/download", methods=['POST'])
def download():
    filename = request.form.get('filename')
    filepath = 'collectorFile/'
    res= make_response(send_from_directory(filepath, filename.encode('utf-8').decode('utf-8'), as_attachment=True))
    res.headers["Content-Disposition"] = "attachment; filename={""}".format(filename.encode().decode('latin-1'))
    return res


# index
@dataCollector.route("/getAll", methods=['GET'])
def index():
    return jsonify("爬虫", 200, 'hello')


