import logging
import allure
import sys
import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
sys.path.append("C:\\Users\\86137\\Desktop\\camp_study_interface")
import jsonpath
from xToolkit import  xfile
import  requests
#import xlrd
import  pytest
import g_varlibles
# from aek.g_varlibles import g_var
from string import  Template


data_excels = xfile.read("data_excel.xls").excel_to_dict()
# print(data_excels)

# 接口请求 = requests.request(method=data_excels[0]["请求方式"],
#                  url=data_excels[0]["接口URL"],
#                  params=eval(data_excels[0]["url参数"]),
#                  json=eval(data_excels[0]["JSON参数"]))
#
# print(接口请求.text)


@pytest.mark.parametrize("case_info",data_excels)
def test_case_excel(case_info):

    allure.dynamic.title(case_info["用例编号"])
    allure.dynamic.title(case_info["描述"])
    url = case_info["接口URL"]

    if "$" in url:
        url = Template(url).substitute(g_varlibles.g_var().show_dict())
        print(url)


    response = requests.request(
        method=case_info["请求方式"],
        # url=case_info["接口URL"],
        url=url,
        params=eval(case_info["url参数"]),
        json=eval(case_info["JSON参数"])
    )
    print(response.text)
    # logging.log(url+"接口返回："+response.text)
    print("----------------------"+url)

    if case_info["提取参数"] != "" or case_info["提取参数"]!=None:
        #assert isinstance(g_var().set_dict, object)
        g_varlibles.g_var().set_dict(case_info["提取参数"], jsonpath.jsonpath(response.json(), '$..' + case_info['提取参数'])[0])
    assert response.status_code == case_info["预期状态码"],"状态码和预期不符合"


#op
if __name__ == '__main__':

    # pytest.main(['-vs','--capture=sys','get_excel.py','--clean-alluredir','--alluredir=allure_results'])
    # os.system(r"allure generate -c -o 测试报告")
    pytest.main(['-s', '-q', 'get_excel.py', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate -c -o allure-report")
    # os.system(r"allure generate ../testoutput/result/ -o ../testoutput/report/ allure-report")
