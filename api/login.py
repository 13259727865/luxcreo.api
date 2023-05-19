#!/usr/bin/env python
# -*-coding:utf-8 -*-
import urllib

# Author:Gemini


from base import readyaml
from base import mainpage
from logs_config import root_log


class Login(mainpage.HttpClient):


    def studio_sso(self):
        root_log.info(f"获取SAMLRequest")
        # 获取项目SAMLRequests
        url = self.api_url["sso"]
        response = self.session.get(url, allow_redirects=False)
        location = response.headers.get('location')
        SAMLRequest = location.split('?')[1].split('&')[0].split('=')[1]
        SAMLRequest = urllib.parse.unquote(SAMLRequest)
        return SAMLRequest

    def auth_sign(self, username, password, type='password'):
        root_log.info(f"开始调用登录接口")
        try:
            # account登录
            url = self.api_url["login"]
            params = {
                'type': type,
                'username': username,
                'password': password,
                'SAMLRequest': self.studio_sso()
            }
            response = self.session.post(params=params, url=url, is_host='account')

            acs_url = response.json()['acsUrl']
            acs_response = self.session.get(url=acs_url, is_host=False)
            if acs_response.status_code == 200:
                root_log.info(f"登陆成功")
            return acs_response.cookies.get_dict()
        except:
            root_log.info(f"登陆失败，请检查参数")




if __name__ == '__main__':
    a = Login()
    a.auth_sign('13259727865','1234qwer')

    print("测试！")
