#!user/bin/env python3
# -*- coding: gbk -*-

import requests
from camp_study_interface.aek.common.config_data import TEST_IP

header = {
    'Content-Type':'application/json;charset=UTF-8',
    'x-auth-token':'2b03a175-8191-4997-88ac-e382ca1a8a91'
}
param = {"warehouseId":"7D0583F8B8D04C73B6509C40204B2322","pageSize":30,"current":1,"comboId":"4","comboType":"4","comboName":"全部物资","channelRequestType":"vwork-local"}

url = TEST_IP+'/vwork/purchase/apply/pscList'
ss = requests.post(url=url,headers=header,json=param)

print(ss.text)
