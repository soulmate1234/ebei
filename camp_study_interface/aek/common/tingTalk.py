
# -*- coding: UTF-8 -*-
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests,json

#加签
webhook='https://oapi.dingtalk.com/robot/send?access_token=91c23eda267936cd36af8412935118468ad948f32c45386dcb145207d112f13e' #钉钉机器人webhook
timestamp = str(round(time.time() * 1000))
secret = 'SECde753f71f0114d2828ae8f56dc77e19b6177128ff94222effa4d530272a23f1f'  #钉钉机器人秘钥
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
# print(string_to_sign)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)
webhook=webhook+'&timestamp='+timestamp+'&sign='+sign
print(webhook)
#定义数据类型
headers={'Content-Type':'application/json'}
data={"msgtype":"text","text":{"content":'接口自动化测试报告：'},"isAtAll":True}
#发送post请求
res=requests.post(webhook,data=json.dumps(data),headers=headers)

print(res.text)
