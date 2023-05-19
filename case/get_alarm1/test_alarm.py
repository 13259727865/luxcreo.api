#!/usr/bin/env python
# -*-coding:utf-8 -*-
import os

# Author:Gemini
import jsonpath
import pymysql
import pytest
import sys
from os.path import dirname

from api.login import Login
from api.studio.studio_api import History, StudioApi

sys.path.append(dirname(dirname(dirname(__file__))))
from api_action.vehicle_alarm import VehicleAlarm
from base.readyaml import ReadYaml
import allure
data = ReadYaml("data", "login_data.yaml").readyaml()

@allure.feature("报警查询用例类")
class TestAlarm:

    # @pytest.mark.parametrezr("user,pw",data["login"])
    def setup_class(self):
        # # con = pymysql.connect(host="127.0.0.1", port=3306, user="dev", password="productdev123")
        # # print("链接数据库")
        # # self.cur = con.cursor()
        # params = data["login"]
        # # user = "hanc"
        # # pw = "NWVhN3Vtc2RmYnRhZWRtaXBuMDVzcWR6dzZxaWh2cXA4Mw=="
        # print(params[0][0], params[0][1])
        # self.alarm = VehicleAlarm(params[0][0], params[0][1])
        Login().auth_sign('13259727865','1234qwer')
        self.history = StudioApi()

    def teardown_class(self):
        # self.cur.close()
        pass

    @allure.story("时间，车辆输入")
    @pytest.mark.parametrize("start_time,end_time,vehicle_id,count", data["get_alarm"], ids=data["ids"])
    def test_get_alarm(self, start_time, end_time, vehicle_id, count):
        self.history.history()



if __name__ == '__main__':
    pytest.main(['-s', '[测试文件.py]', '--alluredir', './allure-result'])
    os.system('allure generate ./allure-result -0 ./reports')