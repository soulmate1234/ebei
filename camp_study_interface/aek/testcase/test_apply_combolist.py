# -*- coding: utf-8 -*-
import allure
import jsonpath
from camp_study_interface.aek.service.apply_combolist_service import ApplyComboListService
from camp_study_interface.aek.common.config_data import pscIdOne,pscIdTwo,warehouseIdTwo
from camp_study_interface.aek.common.log import Log

class TestApplyComboList:

    @allure.story("请领套餐")
    def test_combo_list(self):
        allure.dynamic.title("请领套餐列表查询")
        response = ApplyComboListService().apply_combox_list_service(warehouseIdTwo)
        Log().log_info("请领套餐列表查询" + response.text)
        code = jsonpath.jsonpath(response.json(), '$.code')
            # print(str(code[0]))
        assert str(code[0]) == '200'


    @allure.story("请领套餐")
    def test_combo_add(self):
        allure.dynamic.title("请领增加套餐")
        comboName = "autotest"
        response = ApplyComboListService().apply_combox_add_service(comboName,warehouseIdTwo)
        Log().log_info("请领增加套餐" + response.text)
        code = jsonpath.jsonpath(response.json(), '$.code')
    # print(str(code[0]))
        assert str(code[0]) == '200'
        # 增加套餐列表查询刚才新增的autotest 的套餐

    @allure.story("请领套餐")
    def test_combo_add_goods(self):
        allure.dynamic.title("请领套餐增加物资")
        comboName = "autotest"
        response = ApplyComboListService().apply_combox_add_service(comboName, warehouseIdTwo)
        Log().log_info("请领增加套餐" + response.text)
        code = jsonpath.jsonpath(response.json(), '$.code')
        # print(str(code[0]))
        assert str(code[0]) == '200'


    @allure.story("请领套餐")
    def test_combo_delete_goods(self):
        allure.dynamic.title("请领套餐物资删除")
        comboName = "autotest"
        response = ApplyComboListService().apply_combox_add_service(comboName, warehouseIdTwo)
        Log().log_info("请领增加套餐" + response.text)
        code = jsonpath.jsonpath(response.json(), '$.code')
        # print(str(code[0]))
        assert str(code[0]) == '200'



if __name__ == '__main__':
    TestApplyComboList().test_combo_add()
    # pytest.main()