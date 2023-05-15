import requests

from main_api import main_api


class StudioPage(main_api):

    def __init__(self):
        self.seession = requests.session()
        self.seession.cookies = requests.utils.cookiejar_from_dict(self.login())

    def login(self):
        pass
