# coding:utf-8
from flask import Blueprint, render_template, jsonify, request
from werkzeug.utils import secure_filename

import os

# 创建一个蓝图对象
uploader = Blueprint("uploader", __name__)

# 在生产环境中弃用
@uploader.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                            "uploadfile." + secure_filename(f.filename)))
        return 'single uploaded successfully'


@uploader.route("/uploadmultiple", methods=['POST'])
def uploadMultiple():
    if request.method == 'POST':
        f = request.files.getlist('file')
        for fs in f:
            fs.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                                 "uploadfile." + secure_filename(fs.filename)))

        return 'multiple uploaded successfully'


@uploader.route("/")
def uploadPage():
    return render_template("upload.html")

# 目前采取单份传输的办法
@uploader.route("/uploadCV", methods=['POST'])
def uploadCV():
    if request.method == 'POST':

        f = request.files['file']
        f.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                            "uploadfile." + secure_filename(f.filename)))



        return 'single uploaded successfully'