# -*- coding:utf-8 -*-
from base import BaseApi
from BaseCase import env

class SendSmsCode(BaseApi):
    api_url_smcCode = "/v1/api/common/getSmsCode"

    def send_smsCode_data(self, mobile, token):
        smsCode_data = {"phoneNum":mobile,"token":token,'imageCode': "abcd","smsTemplateCode":"100","operationType":"register"}
        smsCode_data.update(self.build_base_param())
        return smsCode_data


    def send_smsCode(self,mobile, token):
        # 获取图形验证码
        self.get_imageCode(token)
        # 获取短信验证码
        smsCode_data = self.send_smsCode_data(mobile, token)
        print("发送短信验证码完整数据：",smsCode_data)
        full_api_url_smsCode = env.base_api + self.api_url_smcCode
        print("发送短信验证码完整URL",full_api_url_smsCode)
        res = self.post_common(full_api_url_smsCode, smsCode_data)
        return res


# token = BaseApi().get_token()
# s = SendSmsCode()
# print(s.send_smsCode('18618530013',token))