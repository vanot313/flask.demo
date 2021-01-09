# coding:utf-8
from flask import Blueprint, render_template, jsonify, request
from common.models.user import User
from common.models.account import Account
from werkzeug.utils import secure_filename
from services import csvHandler


import os

# 创建一个蓝图对象
uploader = Blueprint("uploader", __name__)


@uploader.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                            "uploadfile."+secure_filename(f.filename)))
        return 'single uploaded successfully'

@uploader.route("/uploadmultiple", methods=['POST'])
def uploadMultiple():
    if request.method == 'POST':
        f = request.files.getlist('file')
        for fs in f:
            fs.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                            "uploadfile." + secure_filename(fs.filename)))

        csvHandler.buildVertifyFile()

        return 'multiple uploaded successfully'

@uploader.route("/")
def uploadPage():
    return render_template("upload.html")
