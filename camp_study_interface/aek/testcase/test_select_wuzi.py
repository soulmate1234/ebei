#!user/bin/env python3
# -*- coding: gbk -*-
import allure
import jsonpath
from camp_study_interface.aek.service.select_wuzi_service import SelectWuziService

class TestSelectWuzi:
    @allure.story("测试Demo")
    def test_selectwuzi(self):
        allure.dynamic.title("测试用例title")
        with allure.step("步骤1：调用接口"):
            response = SelectWuziService().select_wuzi_service_demo()
            code =jsonpath.jsonpath(response.json(),'$.code')
            # print(str(code[0]))
        with allure.step("步骤2：判断结果"):
            assert str(code[0]) == '200'
