# -*- coding:utf-8 -*-
from base import BaseApi
import unittest
from BaseCase import env


class LoginBaseApi(unittest.TestCase,BaseApi):
    api_url_login = '/v1/api/user/login'

    @classmethod
    def setUpClass(cls):
        BaseApi().__init__()
        cls.b = BaseApi()
        cls.login_name = env.mobile_login
        cls.password = env.pw_login
        cls.token = cls.b.get_token()
        print("token信息为：",cls.token)

    def test_login(self):
        full_api_url_login = env.base_api + self.api_url_login
        print("full_api_url_login地址为：",full_api_url_login)
        data = {'phoneNum':self.login_name,'passWord':self.password,'token':self.token}
        self.response = BaseApi().post_base_parameter(url=full_api_url_login,data=data)
        print(self.response)
        globals()['self.access_token'] =self.response['model']['accessToken']
        print(globals()['self.access_token'])
        return globals()['self.access_token']

    def test_m(self):
        print("111111111-1111111")
        print(globals()['self.access_token'])


if __name__ =="__main__":
    unittest.main(verbosity=2)
