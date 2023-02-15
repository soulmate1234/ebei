# -*- coding: utf-8 -*-

import requests
from camp_study_interface.aek.common.comm_request import RequestHttp


class SelectWuziService:

    def select_wuzi_service_demo(self):
        url = '/vwork/purchase/apply/pscList'
        param = {"warehouseId": "7D0583F8B8D04C73B6509C40204B2322",
                 "pageSize": 30, "current": 1, "comboId": "4", "comboType": "4", "comboName": "全部物资",
                 "channelRequestType": "vwork-local"}
        response = RequestHttp.request_post(url, param)
        return response
