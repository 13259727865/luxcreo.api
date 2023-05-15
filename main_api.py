import urllib.parse

import requests


class main_api:

    def __init__(self):
        self.session = requests.session()

    def studio_sso(self):
        #获取项目SAMLRequests
        url = "/v1/auth/sso?RelayState=<RelayState>"
        response = self.session.get(url, allow_redirects=False)
        location = response.headers.get('location')
        SAMLRequest = location.split('?')[1].split('&')[0].split('=')[1]
        SAMLRequest = urllib.parse.unquote(SAMLRequest)
        return SAMLRequest

    def auth_sign(self):
        #account登录
        url = "/v1/sign"
        params = {
            'type': 'password',
            'username': '13259727865',
            'password': '1234qwer',
            'SAMLRequest': self.studio_sso()
        }
        response = self.session.post(params=params, url=url, is_host='account')

        acs_url = response.json()['acsUrl']
        acs_response = self.session.get(url=acs_url, is_host=False)
        return acs_response.cookies.get_dict()

    def history(self):
        #历史记录接口
        url = "/v1/workspace/history?page=1&size=10"
        cookie = self.auth_sign()
        print(cookie)
        headers = {
            "Set-Cookie": cookie
        }
        response = self.session.get(url=url)
        print(response)


if __name__ == '__main__':
    print(main_api().history())
