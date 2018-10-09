# -*- coding:utf-8 -*-
import urllib
from urllib import request,parse
import json
from BaseCase import env
from try_error import *



class BaseApi(object):
    api_url = "/v1/api/common/getToken"
    base_url = env.base_api

    # @classmethod
    # def setUpClass(cls):
    def __init__(self):
        self.response = None
        # self.base_url = env.base_api

    # 拼接url
    def get_full_api_url(self):
        if not self.api_url:
            raise RuntimeError("no url been set")
        return self._get_url()

    # 拼接url
    def get_full_url(self, api_url):
        if not self.api_url:
            raise RuntimeError("no url been set")
        return self.base_url + api_url

    def _get_url(self):
        return "{0}{1}".format(self.base_url, self.api_url)

    # 封装POST请求类型
    def post_common(self, url,data=None):
        if not data:
            data = {}
        data = bytes(urllib.parse.urlencode(data), encoding="utf-8")
        try:
            request = urllib.request.Request(url=url, data=data)
            res = urllib.request.urlopen(request)
            self.response = json.loads(res.read())
            return self.response
        except Exception as e:
            request_error(e)


    def post_base_parameter(self,url, data=None):
        if not data:
            data = {}
        base_param = self.build_base_param()
        custom_param = self.build_custom_param(data)
        data.update(base_param)
        data.update(custom_param)
        print('传递的参数data为：', data)
        data = bytes(urllib.parse.urlencode(data), encoding='utf8')
        request = urllib.request.Request(url=url, data=data)
        try:
            res = urllib.request.urlopen(request)
            response = json.loads(res.read())
            return response
        except Exception as e:
            request_error(e)

    # 封装GET请求类型
    def get_common(self,url,data=None):
        if not data:
            data = {}
        params = urllib.parse.urlencode(data)
        url=url+"?"+params
        print("get_common请求的完整URL", url)
        request = urllib.request.Request(url=url, method='GET')
        try:
            self.response = urllib.request.urlopen(request)
            return self.response
        except Exception as e:
            request_error(e)



    # 封装GET请求类型
    def get_base_common(self,url,data=None):
        if not data:
            data={}
        base_param = self.build_base_param()
        custom_param = self.build_custom_param(data)
        data.update(base_param)
        data.update(custom_param)
        # 序列化所有对应的data数据
        params = urllib.parse.urlencode(data)
        url_new = url + "?" + params
        # 构建request请求头
        request = urllib.request.Request(url=url_new, data=data)
        try:
            self.response = urllib.request.urlopen(request)
            # # 获取返回的字典
            # res = json.loads(self.response.read().decode('utf-8'))
            return self.response
        except Exception as e:
            request_error(e)


    # 获取HTTP状态码
    def get_status_code(self):
        if self.response:
            return self.response.status

    # 获取response中的code的信息
    def get_code(self):
        if self.response:
            return self.response['code']

    #  获取response中的message的信息
    def get_message(self):
        if self.response:
            return self.response['msg']

    # 所有接口共有的入参，比如：app_version、token等
    # 不通的类继承这个基类，如果需要不通的公共参数，需要重写这个方法
    def build_base_param(self):
        return {
                "client": 1,
                "platform":"HLW"
        }

    # 被测接口除公共参数外所需的其余参数
    def build_custom_param(self, data):
        if not data:
            return {}
        else:
            return data

    # 获取model字段下面某个字段的value
    def get_info_by_name(self, info_name):
        info = self.response['model'][info_name]
        return info

    def get_response_type(self):
        return type(self.response)

    def get_token(self):
        api_url_token = "/v1/api/common/getToken"
        full_api_url_token = self.base_url+api_url_token
        res = self.post_common(full_api_url_token)
        token = res['model']['token']
        return token

    def get_imageCode(self, token):
        api_url_imageCode = "/v1/api/common/getValidateImage"
        full_api_url_imageCode = self.base_url + api_url_imageCode
        print("发送图形验证码完整URL:",full_api_url_imageCode)
        token_data = {"token":token}
        res = self.get_common(full_api_url_imageCode, token_data)
        print("发送图形验证码结果：",res.status)
        return res

    def get_userCode(self, mobile):
        api_url_userStatus = "/v1/api/userQuery/checkUserByMobile"
        full_api_url_userStatus = self.base_url + api_url_userStatus
        mobile_data = {"mobile":mobile}
        res = self.post_common(full_api_url_userStatus, data=mobile_data)
        usercode = res["model"]["userCode"]
        return usercode

if __name__ =="__main__":
    b = BaseApi()
    print(b.get_full_api_url())
    print(b.get_token())
#     data = {'phoneNum': '18616300003', 'passWord': 'C3pwf3Cz/0Ofk/QV7CHWvA==', 'token': '47a9c322d1724b9bb8c4864c3e155591', 'client': 1, 'platform': 'HLW'}
#
#     r = b.post_base_parameter(url='http://192.168.7.228:8098/v1/api/common/getToken',data=data)
#     print(r)



#     data = {'word': 'hello'}
#     url = b.get_full_api_url()
#     print("full_url:", url)
#     print(b.post_common(url, data))
    # #
    # # print(b.get_info_by_name('token'))
    # token = b.get_token()
    # print(token)
    # print(b.get_imageCode(token))

    # url = "http://api-test2.chinazyjr.net/v1/api/common/getValidateImage"
    # token = b.get_token()
    # data = {"token": token}
    # r = b.get_common(url,data)
    # print(r.status)

    # token = b.get_token()
    # b.get_imageCode(token)

