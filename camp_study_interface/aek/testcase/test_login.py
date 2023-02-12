# -*- coding: utf-8 -*-
import os

import allure
import pytest
import requests
from camp_study_interface.aek.common.config_data import TEST_IP, userLoginName, userLoginPassword

s = requests.session();


class TestLogin():
    @allure.story("登录")
    def test_login(self):
        ip = TEST_IP;
        url = ip + '/vwork/login'
        param = {
            'userLoginName': userLoginName,
            'userLoginPassword': userLoginPassword
        }
        response = s.post(url=url, json=param)
        assert 1==1

    def test_one(self):
        print("hello")
        q=1
        w=2
        assert  q==w
    if __name__ == '__main__':

        pytest.main(['-s', '-q', 'test_login.py', '--clean-alluredir', '--alluredir=allure-results'])
        os.system(r"allure generate -c -o allure-report")


