import os
from util import str_tools


class Uploader:
    def __init__(self):
        pass

    def upload_single(self, file):
        filename = str_tools.ranstr(20) + ".csv"

        file.save(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./uploadfile")),
                               filename))

        return filename
