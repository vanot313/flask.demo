import os
from flask import *
from util import str_tools


class FileHandler:
    def __init__(self):
        pass

    def upload_single(self, file):
        filename = str_tools.ranstr(20) + ".csv"

        file.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                               filename))
        print(filename)
        return filename

    def download_file(self, filename):

        try:
            if os.path.isfile(os.path.join('uploadfile', filename)):
                return send_file(os.path.join('uploadfile', filename), as_attachment=True)
        except:
            abort(404)
        abort(404)

        # path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")))
        #
        # if os.path.isfile(os.path.join(path, filename)):
        #     return send_from_directory(path, filename, as_attachment=True)
        #
        # return send_from_directory(path, filename, as_attachment=True)
