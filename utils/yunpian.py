# -*- coding: utf-8 -*-
__author__ = 'JUN SHANG'
__date__ = '2019/1/22 0022 上午 6:23'
import requests
import json


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile, ):
        param = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': "【天瑞仪器】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }

        response = requests.post(self.single_send_url, data=param)
        print(response.text)
        return json.loads(response.text)


if __name__ == "__main__":
    yun_pian = YunPian("2244c6946f6bdb84f126286e9ff084d7")
    yun_pian.send_sms("2017", "1351836755")
