# -*- coding:utf-8 -*-
import unittest
from user_controller import *
from read_database import *
import re
import time


class Register_Login_ForgetPW(unittest.TestCase,BaseApi):

    @classmethod
    def setUpClass(cls):
        print("Register_Login_ForgetPW测试用例开始执行")

    def test_101_register(self):
        """先在数据库添加一条数据，然后再从数据库读取新的注册手机号"""
        add_register_info()
        id_new = read_last_info()[0]
        r = RegisterApi(id_new)
        msg = r.register()
        self.assertEqual(msg,"注册成功！")

    def test_102_register(self):
        """注册时候，从数据库里面读取最新的已注册的手机号"""
        id_new = read_last_info()[0]
        r = RegisterApi(id_new)
        msg = r.register()
        self.assertEqual(msg, "您已在中赢金融旗下【好利网】平台注册，本平台将不能注册开通存管。")

    def test_201_forget_pw(self):
        """登录之前的时候忘记密码---修改密码（新老密码一致）"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()

        f = ForgetPassWord(mobile_new,pw_1)
        msg = f.forget_password()
        self.assertEqual(msg,"新密码与原密码不能相同")

    def test_202_forget_pw(self):
        """登录之前的时候忘记密码---修改密码（新老密码不一致）"""
        id_new,mobile_new,pw_1,pw_2 = read_last_info()
        pw_new = "A123456"      # 需要最终修改的密码

        f = ForgetPassWord(mobile_new,pw_new)
        msg = f.forget_password()

        if msg =="成功":
            updata_jiamiPW_info(id_new,pw_new)
            print("更新密码（密文）成功")

    def test_203_login(self):
        """登录操作--正常路径"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        l = Login(mobile_new,pw_1)
        msg = l.login()[1]
        print(msg)
        self.assertEqual(msg,"成功")

    def test_204_login(self):
        """登录操作--密码输入错误3次之后，再输入正确密码，依然可以登录"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        error_pw = "b123456"
        l = Login(mobile_new,error_pw)
        num = 0
        while num < 5:
            time.sleep(0.5)
            msg = l.login()[1]
            print(msg)
            error_num = re.match(".+已错误(\d)", msg)
            print("error_num的信息为：",error_num)
            if error_num:
                num = int(error_num.group(1))
                print("num的值为：", num)
                if num==3:
                    break
            else:
                print("正则表达式没有配到最终的数据，msg数据为: %s"%msg)
                break
        # 断言，错误3次之后，还可以正常登陆
        l_right = Login(mobile_new,pw_1)
        msg_new = l_right.login()[1]
        self.assertEqual(msg_new,"成功")

    def test_205_login(self):
        """登录操作--密码输入再1次错误，错误次数是1"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        error_pw = "b123456"
        l = Login(mobile_new, error_pw)
        msg = l.login()[1]
        print(msg)
        error_num = re.match(".+已错误(\d)", msg)
        if error_num:
            num = int(error_num.group(1))
            self.assertEqual(num, 1)
        else:
            print("正则表达式没有pi配到最终的数据，msg数据为%s" % msg)

    def test_206_login(self):
        """登录操作--密码输入3次错误、1次正确，再2次错误，最终不能登录"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        error_pw = "b123456"
        l = Login(mobile_new, error_pw)
        num = 0
        while num < 5:
            msg = l.login()[1]
            print(msg)
            error_num = re.match(".+已错误(\d)", msg)
            if error_num:
                num = int(error_num.group(1))
                if num == 5:
                    break
            else:
                print("正则表达式没有pi配到最终的数据，msg数据为%s" % msg)
                break

        # 断言，错误5次之后，不能正常登陆
        l_right = Login(mobile_new, pw_1)
        msg_new = l_right.login()[1]
        print(msg_new)
        self.assertEqual(msg_new, "密码输入连续错误5次，请30分钟后登录或找回密码")

    def test_207_forget_PW(self):
        """密码输入错误5次之后，点击忘记密码，使用新密码可以再次登录"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        pw_new = 'b123456'
        f = ForgetPassWord(mobile_new,pw_new)
        msg = f.forget_password()
        print(msg)
        if msg == "成功":
            updata_jiamiPW_info(id_new,pw_new)
        elif msg == "新密码与原密码不能相同":
            print("新密码与原密码不能相同,请重新设置密码")
        else:
            print("修改密码失败")
        l = Login(mobile_new, pw_new)
        msg_login = l.login()[1]
        self.assertEqual(msg_login,"成功")

    def test_301_change_PW(self):
        """修改密码(错误路径--新老密码一致)---前端需要登录之后才能点击修改，其实不需要传递accessToken也能修改"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        c = Change_PassWord(mobile_new,pw_1,pw_1)
        code,msg = c.change_password()
        if code=="newpassword_equal_oldpassword":
            print("新密码和原密码相同--请重新输入新密码")
        elif code == "fail":
            print("传递的参数有误，请接口传递值")
        elif code=="password_fail_exception":
            print("原密码错误","msg的值为:%s"%msg)
        elif code == "param_not_right":
            print("新密码格式错误", "msg的值为:%s" % msg)
        elif code == "success":
            print("修改密码成功","msg的值为:%s"%msg)
            updata_jiamiPW_info(id_new,pw_1)
        self.assertEqual(code,"newpassword_equal_oldpassword")

    def test_302_change_PW(self):
        """修改密码(错误路径--原密码错误&新密码格式错误)"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        pw_new = "123456a"
        c = Change_PassWord(mobile_new,pw_new,pw_new)
        code,msg = c.change_password()
        if code=="password_fail_exception":
            print("原密码错误","msg的值为:%s"%msg)
        self.assertEqual(code,"password_fail_exception")
        # 新密码使用错误格式"123456",最终断言
        pw_new2 = "123456"
        c2 = Change_PassWord(mobile_new, pw_new, pw_new2)
        code2, msg2 = c2.change_password()
        if code2 =="param_not_right":
            print("新密码格式错误","msg的值为:%s"%msg2)
        self.assertEqual(code2,"param_not_right")

    def test_303_change_PW(self):
        """修改密码（正确路径）"""
        id_new, mobile_new, pw_1, pw_2 = read_last_info()
        pw_new = "c123456"
        c = Change_PassWord(mobile_new,pw_1,pw_new)
        try:
            code,msg = c.change_password()
            if code == "success":
                print("修改密码成功","msg的值为:%s"%msg)
                updata_jiamiPW_info(id_new,pw_new)
            self.assertEqual(code,"success")
        except Exception as e:
            print("捕获到错误信息：%s"%e)


if __name__ =="__main__":
    unittest.main()

