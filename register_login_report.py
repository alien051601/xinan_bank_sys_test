from BeautifulReport import BeautifulReport
import unittest
from register_login_forgetpw import Register_Login_ForgetPW
import os
import time

current_path = os.getcwd()
report_path = os.path.join(current_path, "Report_HTML/Register")
now_str = str(time.strftime("%Y%m%d-%H-%M", time.localtime(time.time())))

# 报告地址&名称
report_title = now_str + '注册登录忘记密码'

# 报告描述
desc = '注册&登录&忘记密码----接口自动化'


if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.makeSuite(Register_Login_ForgetPW))
    run = BeautifulReport(testsuite)
    run.report(description=desc, filename=report_title,log_path=report_path)
