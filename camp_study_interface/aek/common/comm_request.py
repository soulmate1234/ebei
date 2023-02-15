# -*- coding: gbk -*-

import requests
from camp_study_interface.aek.common.config_data import TEST_IP
from camp_study_interface.aek.testcase.test_login  import TestLogin


class RequestHttp:
    def request_post(url,param):
        s = TestLogin().test_login()
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'x-auth-token': s
        }
        url = TEST_IP + url
        response = requests.post(url=url,headers=header,json=param)
        return response


