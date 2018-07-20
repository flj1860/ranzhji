# coding = utf-8
#__author__ : will
import unittest,time
from common.HTMLTestRunner_cn import HTMLTestRunner
from case.test_add import Test_add

test_suite = unittest.TestSuite()
test_suite.addTest(Test_add('test_add'))
print(test_suite)

current = time.strftime('%Y%m%d %H_%M_%S')
reportpath = 'D:\\Py\\sele\\report' + '\\report%s.html'%current

fp = open(reportpath,'wb')

runner = HTMLTestRunner(fp,
                        verbosity=2,
                        title='这是我的报告',
                        description='报告内容如下',
                        retry=1)   #retry  失败后用例重跑
runner.run(test_suite)