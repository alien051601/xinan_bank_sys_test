# -*- coding:utf-8 -*-
from read_database import read_register_info
from send_sms_code import *
from jiami import *
from base import BaseApi
from read_excel import read_excel_for_rlf
import json
from try_error import *

# 注册账号
class RegisterApi(BaseApi):
    api_url = '/v1/api/user/register'

    def __init__(self,row_num):
        super(RegisterApi).__init__()
        # 从数据库读取需要的基本数据
        k = read_register_info(row_num)
        self.mobile = k["register_mobile"]
        self.pw = k['register_pw1']
        self.token = BaseApi().get_token()

    def register_prepare(self):
        # 对密码加密
        p = Prpcrypt()
        pw_16 = p.pad(self.pw)
        pw_jiami = p.jiami(pw_16)

        register_data={"phoneNum":self.mobile,"passWord": pw_jiami,"token":self.token,"imageCode": "abcd","SmsCode": "123456","version":"1.0.0"}
        register_data.update(self.build_base_param())
        print("注册需要的全部数据：", register_data)
        return register_data

    def register(self):
        url = self.get_full_api_url()
        print("注册的完整网址:",url)

        # 发送短信验证码(附带图形验证码)
        s = SendSmsCode()
        s.send_smsCode(self.mobile,self.token)
        data = self.register_prepare()
        res = self.post_common(url,data)
        print("注册时返回的完整数据：",res)
        return res['msg']

    # 读取excel里面的数据并注册
    def read_register_data_excel(self,row_num):
        try:
            data = read_excel_for_rlf(int(row_num))[0]
            data_dict = json.loads(data)
        except Exception as e:
            read_excel_error(e)

        else:
            url = self.get_full_api_url()
            data_dict.update({"token":self.token})
            print('read_register_data_excel的全部数据为：',url,data_dict)

            # 发送短信验证码(附带图形验证码)
            s = SendSmsCode()
            s.send_smsCode('18616300007',self.token)

            res = self.post_common(url,data_dict)
            msg = res['msg']
            print("读取excel注册的完整结果为：",res)
            return msg

# 忘记登录密码
class ForgetPassWord(BaseApi):
    api_url = '/v1/api/user/forgetPassWord'

    def __init__(self,mobile,pw_new):
        super(ForgetPassWord).__init__()
        self.mobile = mobile

        #对密码加密
        p = Prpcrypt()
        pw_16 = p.pad(pw_new)
        self.pw_jiami = p.jiami(pw_16)

    def forget_password_prepare(self):
        token = BaseApi().get_token()
        register_data = {"phoneNum": self.mobile, "passWord": self.pw_jiami, "token": token, 'imageCode': "abcd", 'SmsCode': "123456",}
        register_data.update(self.build_base_param())

        # 发送短信验证码(附带图形验证码)
        s = SendSmsCode()
        s.send_smsCode(self.mobile, token)
        return register_data

    def forget_password(self):
        url = self.get_full_api_url()
        data = self.forget_password_prepare()
        print("forget_password接口数据：",url,data)
        res = self.post_common(url=url,data=data)
        print("forget_password返回的response：",res)
        return res["msg"]


# 修改登录密码
class Change_PassWord(BaseApi):
    api_url = '/v1/api/user/changePassword'

    def __init__(self,mobile,pw_old,pw_new):
        super(Change_PassWord).__init__()
        self.mobile = mobile

        #对密码加密
        p = Prpcrypt()
        pw_16_old = p.pad(pw_old)
        pw_16_new = p.pad(pw_new)
        self.pw_jiami_old = p.jiami(pw_16_old)
        self.pw_jiami_new = p.jiami(pw_16_new)

    def change_password_prepare(self):
        register_data = {"phoneNum": self.mobile, "oldPassword": self.pw_jiami_old, "newPassword": self.pw_jiami_new, 'newPasswordConfirm': self.pw_jiami_new, 'platform': "HLW",}
        register_data.update(self.build_base_param())

        return register_data

    def change_password(self):
        url = self.get_full_api_url()
        data = self.change_password_prepare()
        print("change_password接口数据：",url,data)
        res = self.post_common(url=url,data=data)
        print("change_password返回的response：",res)
        code = res["code"]
        msg = res["msg"]
        print("msg最终结果为：",msg)
        return code,msg

class Login(BaseApi):
    api_url = '/v1/api/user/login'

    def __init__(self,mobile,pw):
        super(Login).__init__()
        self.mobile = mobile

        #对密码加密
        p = Prpcrypt()
        pw_16 = p.pad(pw)
        self.pw_jiami = p.jiami(pw_16)
        self.token = self.get_token()

    def login(self):
        url = self.get_full_api_url()
        print("login地址为：",url)
        data = {'phoneNum':self.mobile,'passWord':self.pw_jiami,'token':self.token}
        res = self.post_base_parameter(url=url,data=data)
        print("login接口返回的完整数据为：", res)
        if res["msg"]=="成功":
            accessToken = res['model']['accessToken']
            print('accessToken的值为：',accessToken)
            return accessToken,res["msg"]
        else:
            return None,res["msg"]

if __name__ == '__main__':

    # msg = r.read_register_data_excel(4)
    # print(msg)

    # print(dict,type(dict))

    # d = json.dumps(data)
    # print(type(d),d)
    # print(r.register(5, token))
    # data.update({'token':token})
    # print(data)

    # 忘记密码
    # f = ForgetPassWord('18616300005','a123456')
    # f.forget_password()

    # 修改密码
    # c = Change_PassWord('18616300004','A123456','A123456')
    # c.change_password()

    # 登录
    l = Login("18616300004",'A123456')
    l.login()






# API使用函数如下：
def register_new(num):
    r = RegisterApi()
    token = r.get_token()
    result = r.register(num, token)
    return result

# register_new(2)
