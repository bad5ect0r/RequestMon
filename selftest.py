from requestobj import RequestObj

import requests
import os


class SelfTest(RequestObj):
    def __init__(self):
        RequestObj.__init__(self)
        self.url = 'http://localhost:8000/test.txt'
        self.save_path = './Pages/Example/'
        self.diff_path = './Results/Example/'
        self.ext = ''

        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        if not os.path.exists(self.diff_path):
            os.makedirs(self.diff_path)

    def request(self):
        return requests.get(self.url)

