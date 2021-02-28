import os
from util import strTools


class Uploader:
    def __init__(self):
        pass

    def upload_single(self, file):
        filename = strTools.ranstr(20) + ".csv"

        file.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                               filename))

        return filename
