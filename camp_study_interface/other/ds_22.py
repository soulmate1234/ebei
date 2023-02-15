import requests
import jsonpath

"""
值的传递 -- 四要素
postman jmeter .... 
requests : 
params-- 参数写在url上，用它
data -- 字典类型
json -- 对请求头有要求，Applicaiton/json
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
rs= requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",data=data,params=params)
ls = jsonpath.jsonpath(rs.json(),'$..token')
rs1 = requests.post(url="http://shop-xo.hctestedu.com/index.php?"
                        "s=/api/cart/save&token={}".format(ls[0]),data=data2,params=params)

print(rs1.text)
"""
加密接口？ --怎么测试的？
抓包 -- 问前端 aa,bb,cc
1000个接口？怎么测试？ --进阶 进化?
"""