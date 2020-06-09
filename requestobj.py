from diff2HtmlCompare.diff2HtmlCompare import CodeDiff

import requests
import time
import os


class RequestObj:
    def __init__(self):
        pass

    def save(self):
        self.filename = str(int(time.time())) + self.ext

        with open(self.save_path + self.filename, 'w') as f:
            f.write(self.response.text)

        self.downloaded = True

    def perform_request(self):
        self.response = self.request()

    def is_different_to_file(self, filepath):
        assert self.response

        fcontents = ''
        with open(filepath, 'rb') as f:
            fcontents = f.read()

        return fcontents != self.response.text.encode('utf-8')

    def generate_diff(self, filepath, options):
        output = self.diff_path + self.filename + '.html'
        codeDiff = CodeDiff(filepath, self.save_path + self.filename + self.ext, name=self.filename)
        codeDiff.format(options)
        codeDiff.write(output)

        return output

    def is_x_files_present(self, count):
        return len(os.listdir(self.save_path)) >= count

