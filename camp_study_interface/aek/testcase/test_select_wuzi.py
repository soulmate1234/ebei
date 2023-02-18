#!user/bin/env python3
# -*- coding: gbk -*-
import allure
import jsonpath
from camp_study_interface.aek.service.select_wuzi_service import SelectWuziService

class TestSelectWuzi:
    @allure.story("����Demo")
    def test_selectwuzi(self):
        allure.dynamic.title("��������title")
        with allure.step("����1�����ýӿ�"):
            response = SelectWuziService().select_wuzi_service_demo()
            code =jsonpath.jsonpath(response.json(),'$.code')
            # print(str(code[0]))
        with allure.step("����2���жϽ��"):
            assert str(code[0]) == '200'
