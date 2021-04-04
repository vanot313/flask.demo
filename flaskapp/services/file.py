import os
from flask import *
from util import str_tools
from util.response import *


class FileHandler:
    def __init__(self):
        pass

    def upload_single(self, file, path):
        filepath = str_tools.ranstr(20) + ".csv"

        file.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile" + "/" + path)),
                               filepath))

        filepath = path + "/" + filepath
        return filepath

    def download_file(self, filepath):

        try:
            if os.path.isfile(os.path.join('uploadfile', filepath)):
                return send_file(os.path.join('uploadfile', filepath), as_attachment=True)
            else:
                return response("文件不存在", 404, {})
        except:
            return response("下载失败", 404, {})

        # path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")))
        #
        # if os.path.isfile(os.path.join(path, filename)):
        #     return send_from_directory(path, filename, as_attachment=True)
        #
        # return send_from_directory(path, filename, as_attachment=True)
