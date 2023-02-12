import pytest
import os
if __name__ == '__main__':
    # try:
    #     # 删除之前的文件夹
    #     shutil.rmtree("allure-results")
    # except:
    #     print('之前未生成报告原文件')
    # pytest.main([])
    #编译报告原文件并启动报告服务
    # os.system('allure serve report/allure_raw')
    # os.system('allure serve allure-results')

    current_working_dir = os.getcwd()
    print(f"当前工作路径: {current_working_dir}")
    str1 = current_working_dir+r"\allure-results"
    str = f"--alluredir={str1}"
    print(str)
    pytest.main(['-s', '-q',  '--clean-alluredir', str])
    os.system(r"allure generate -c -o allure-report")

