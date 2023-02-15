# -*- coding = utf-8 -*-
# @time:2023/1/5
# Author:wm

import requests
import jsonpath
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(sys.path)


"""
完成商城从登录到购物车的添加流程
1.学会活用接口四要素读懂接口文档
2.学会利用好对应的requests的参数来解决问题
"""
data = {
    "accounts": "huace_xm",
    "pwd": "123456",
    "type": "username"
}
params = {
    "application": "app",
    "application_client_type": "weixin",
}



data2 = {
    "goods_id": "2",
    "spec": [
        {
            "type": "套餐",
            "value": "套餐二"
        },
        {
            "type": "颜色",
            "value": "银色"
        },
        {
            "type": "容量",
            "value": "64G"
        }
    ],
    "stock": 2
}

#login
rs= requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",data=data,params=params)

#获取登录token
ls = jsonpath.jsonpath(rs.json(),'$..token')
#print(rs.text)
#print(ls)

#加入购物车
rs1 = requests.post(url="http://shop-xo.hctestedu.com/index.php?"
                        "s=/api/cart/save&token={}".format(ls[0]),data=data2,params=params)

print(rs1.text)
