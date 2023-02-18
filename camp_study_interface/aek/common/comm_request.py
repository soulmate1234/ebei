# -*- coding: gbk -*-

import requests
from camp_study_interface.aek.common.config_data import TEST_IP,SPD_IP
from camp_study_interface.aek.testcase.test_login  import TestLogin


class RequestHttp:
    def request_post(url,param,type):
        s = TestLogin().test_login()
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'x-auth-token': s
        }
        if type == 'vwork':
            url = TEST_IP + url
        else:
            url = SPD_IP + url

        response = requests.post(url=url,headers=header,json=param)
        return response

    def request_get(url,param,type):
        s = TestLogin().test_login()
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'x-auth-token': s
        }
        if type == 'vwork':
            url = TEST_IP + url + param
        else:
            url = SPD_IP + url + param
        response = requests.get(url=url, headers=header)
        return response

