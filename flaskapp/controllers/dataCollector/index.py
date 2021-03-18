# coding:utf-8
from flask import *
from application import db
from common.models.crawler import Crawler
import random

from services import ServicesContainer
from util import str_tools, response
import subprocess
import os

from util.response import serialize

dataCollector = Blueprint("dataCollector", __name__)


# 上传代码
@dataCollector.route("/upload", methods=['POST'])
def upload():
    name = request.form.get('name')
    filename = request.form.get('filename')
    remark = request.form.get('remarks')
    file = request.files['file']

    if filename is None:
        return response.response("信息不完全", 1002, {})
    path = './webScrapy/webScrapy/spiders/' + filename
    # 保存路径
    file.save(path)
    new_Crawl = Crawler(name=name, filepath=filename, remarks=remark)
    result = ServicesContainer.crawl_handler.add(new_Crawl)
    return response.response("upload success", 200, result)


# 执行爬虫
@dataCollector.route("/execute", methods=['POST'])
def execute():
    status = 1
    output = "nothing"

    name = request.form.get('name')
    outFile = request.form.get('outFile')

    # 判断是否存在爬虫文件夹
    if not os.path.exists("webScrapy"):
        status, output = subprocess.getstatusoutput('scrapy startproject webScrapy')
        if status == 1:
            return jsonify("爬虫框架创建失败", 200, {"status": status,
                                             "output": output})
    if not os.path.exists("collectorFile"):
        os.mkdir('collectorFile')

    if name is None and outFile is None:
        return response.response('请选择文件', 1002, {})

    outFile = '../../../collectorFile/' + outFile
    print(outFile)
    cmd = 'cd ./webScrapy/webScrapy/spiders/ & scrapy crawl ' + name + ' -o ' + outFile
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
        result = ServicesContainer.crawl_handler.getByName(name)
        result.datapath = outFile
        res = ServicesContainer.crawl_handler.update(result)
        return jsonify("爬虫成功", 200, {"status": status, 'data': serialize(res)})


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
    try:
        print(ServicesContainer.crawl_handler.getAll())
        return response.response_multiple('成功', 200, ServicesContainer.crawl_handler.getAll())
    except Exception as e:
        return response.response('查询失败', 1001, {})



