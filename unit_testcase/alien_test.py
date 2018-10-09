import unittest
from BeautifulReport import BeautifulReport
from HTMLTestRunner_PY3 import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner

class Alien_Test(unittest.TestCase):
    def test_1_alien(self):
        print("hello world")

    def test_2_alien(self):
        print("hello world")

    def test_3_alien(self):
        print("hello world")

    def test_4_alien(self):
        print("hello world")

if __name__ == '__main__':
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Alien_Test))
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)


    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(Alien_Test))
    # run = BeautifulReport(suite)
    # run.report('login_tes.html', '登录测试用例')
    # print(run.success_count)  # 通过的次数
    # print(run.failure_count)  # 失败的次数
    pass


