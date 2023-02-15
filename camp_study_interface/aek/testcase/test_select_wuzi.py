#!user/bin/env python3
# -*- coding: gbk -*-
import allure
import jsonpath
from camp_study_interface.aek.service.select_wuzi_service import SelectWuziService
import requests
# from camp_study_interface.aek.common.config_data import TEST_IP
# from test_login import TestLogin
# s = TestLogin().test_login()
# header = {
#     'Content-Type':'application/json;charset=UTF-8',
#     'x-auth-token':s
# }
# param = {"warehouseId":"7D0583F8B8D04C73B6509C40204B2322","pageSize":30,"current":1,"comboId":"4","comboType":"4","comboName":"全部物资","channelRequestType":"vwork-local"}
#
# url = TEST_IP+'/vwork/purchase/apply/pscList'
# # ss = requests.post(url=url,headers=header,json=param)
#
# ss = requests.post(url=url,headers=header,json=param)
#
# print(ss.text)
class TestSelectWuzi:
    @allure.story("测试Demo")
    def test_selectwuzi(self):
        allure.dynamic.title("测试用例title")
        with allure.step("步骤1：调用接口"):
            response = SelectWuziService().select_wuzi_service_demo()
            code =jsonpath.jsonpath(response.json(),'$.code')
            print(str(code[0]))
        with allure.step("步骤2：判断结果"):
            assert str(code[0]) == '200'
