#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
import requests

# from page import login
from api.login import Login
from api.studio.vehicle_alarm import Alarm


class VehicleAlarm:
    def __init__(self,user,pw):
        #业务接口调用前，获取到登录用户session_id
        self.username = user
        self.password = pw
        self.login_rec = Login()
        self.session = {"cookie": f"ponytech_sid={self.login_r()['ponytech_sid']}"}
        # print(self.session)
        self.alarm_rec = Alarm()

    def login_r(self):
        a = self.login_rec.login(self.username, self.password)
        # print("输出：", a.cookies.get_dict())
        return a.cookies.get_dict()

    def vehicle_alarm(self, start_time, end_time, vehicle_id=[]):
        return self.alarm_rec.get_vehicle_alarm(start_time, end_time, vehicle_id=vehicle_id, headers=self.session)

    def vehicle_alarm_count(self, start_time, end_time, vehicle_list=[]):
        return self.alarm_rec.get_alarm_count(start_time, end_time, vehicle_list=vehicle_list, headers=self.session)

    def fileupload(self):
        url = "http://121.40.214.242:8080/ponysafety2/a/fileupload/common"
        files = {
            "file":open("F:/untitled1/pony-api-requests/yaml/Snipaste_2021-05-31_14-03-34.png","rb")
        }
        # de_headers = {"Content-Disposition":"form-data"}
        # headers = de_headers.update(self.session)
        r = requests.post(url=url,body={"key":"contract:123"},files=files,headers=self.session)
        return r.json()

    # def jsonload(self):
    #     a = {'rs': 1, 'reason': None, 'alarmcount_list': [{'name': '1', 'count': 2, 'id': None, 'pct': None}, {'name': '3', 'count': 34, 'id': None, 'pct': None}, {'name': '4', 'count': 39, 'id': None, 'pct': None}, {'name': '5', 'count': 1, 'id': None, 'pct': None}, {'name': '6', 'count': 7, 'id': None, 'pct': None}, {'name': '10', 'count': 241, 'id': None, 'pct': None}, {'name': '104', 'count': 1, 'id': None, 'pct': None}, {'name': '233', 'count': 12, 'id': None, 'pct': None}, {'name': '301', 'count': 417, 'id': None, 'pct': None}]}
    #     print(jsonpath.jsonpath(a,"$.alarmcount_list[0].name"))

if __name__ == '__main__':
    a = VehicleAlarm("hanc","NWVhN3Vtc2RmYnRhZWRtaXBuMDVzcWR6dzZxaWh2cXA4Mw==")
    r = a.vehicle_alarm(start_time="2021-05-25 00:00:00", end_time="2021-05-25 23:59:59",
                        vehicle_id=["242", "187", "199"])
    print(r.json())
    r1 = a.vehicle_alarm_count(start_time="2021-05-25 00:00:00", end_time="2021-05-25 23:59:59",
                               vehicle_list=["242", "187", "199"])
    print(r1.json())
    # print(a.fileupload())
    # a.jsonload()
