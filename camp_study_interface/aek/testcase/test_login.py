# -*- coding: utf-8 -*-
import os

import allure
import pytest
import requests
from camp_study_interface.aek.common.config_data import TEST_IP, userLoginName, userLoginPassword
import logging


s = requests.session()

class TestLogin:

    @allure.story("登录")
    def test_login(self):
        ip = TEST_IP;
        url = ip + '/vwork/login'
        param = {
            'userLoginName': userLoginName,
            'userLoginPassword': userLoginPassword
        }
        response = s.post(url=url, json=param)
        print("---------------------++++++++++++++"+response.text)
        # logging.info("-------------------"+response.text)
        print(response.cookies.values())
        token = response.cookies.values()[0]
        print(token)
        return token


#     def test_one(self):
#         print("hello")
#         q=1
#         w=2
#         assert  q==w
#     def test_2ne(self):
#         print("hello")
#         q=1
#         w=2
#         assert  w==w
#
# if __name__ == '__main__':
#     TestLogin().test_login()
#     pytest.main()