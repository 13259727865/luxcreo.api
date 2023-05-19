#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from base import mainpage
from base.readyaml import ReadYaml


class Alarm(mainpage.HttpClient):

    def __init__(self):
        super(Alarm, self).__init__()
        self.alarm_api = ReadYaml(filetype="api", filename="vehicle_alarm").readyaml()

    def get_vehicle_alarm(self, start_time, end_time, vehicle_id=[], headers={}):
        url = self.alarm_api["get_alarm"]
        method = "post"
        body = {"start_time": start_time,
                "end_time": end_time,
                "max_speed": 150,
                "min_speed": 0,
                "count": 30,
                "page": 1,
                "type": 4,
                "alarmtype_list": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 219, 220,
                                   221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237,
                                   238, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262,
                                   263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 101, 102, 103, 104, 105,
                                   106, 107, 108, 109, 197, 198, 199, 110, 111, 112, 113, 114, 115, 116, 117, 118, 14,
                                   1, 3, 4, 6, 2, 7, 5, 8, 12, 18, 19, 22, 23, 404, 405, 406, 407, 408, 409, 410, 411,
                                   412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428,
                                   429, 430, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                                   52, 55, 56, 57, 58, 59, 60, 61, 301, 302, 303, 304, 305, 306, 307, 308, 601, 602,
                                   603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619,
                                   620, 621, 622, 701, 702, 703, 704, 705, 17, 11, 16, 10, 15, 9],
                "vehicle_id": vehicle_id}
        return self.send(url=url, method=method, body=body, headers=headers)

    def get_alarm_count(self, start_time, end_time, vehicle_list=[], headers={}):
        url = self.alarm_api["get_alarm_count"]
        method = "post"
        body = {"start_time": start_time,
                "end_time": end_time,
                "max_speed": 150,
                "min_speed": 0,
                "count": 30,
                "page": 1,
                "type": 4,
                "alarmtype_list": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 219, 220,
                                   221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237,
                                   238, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262,
                                   263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 101, 102, 103, 104, 105,
                                   106, 107, 108, 109, 197, 198, 199, 110, 111, 112, 113, 114, 115, 116, 117, 118, 14,
                                   1, 3, 4, 6, 2, 7, 5, 8, 12, 18, 19, 22, 23, 404, 405, 406, 407, 408, 409, 410, 411,
                                   412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428,
                                   429, 430, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                                   52, 55, 56, 57, 58, 59, 60, 61, 301, 302, 303, 304, 305, 306, 307, 308, 601, 602,
                                   603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619,
                                   620, 621, 622, 701, 702, 703, 704, 705, 17, 11, 16, 10, 15, 9],
                "vehicle_id": vehicle_list
                }
        return self.send(url=url,method=method,body=body,headers=headers) 

if __name__ == '__main__':
    a = Alarm().get_vehicle_alarm(start_time="2021-05-25 00:00:00", end_time="2021-05-25 23:59:59",
                                  vehicle_id=["25526", "12910", "25534", "25533"],
                                  headers={"Cookie": "ponytech_sid=2121e7f1-40ab-4566-b4fb-647df00853e1"})
    print(a.json())
