#coding=utf-8
import unittest

import time

from base.HTMLTestRunner_cn import HTMLTestRunner
from test_cases.ranzhi_tests import RanzhiTest


class RanzhiTestRunner(object):

    def run(self):
        test_suite = unittest.TestSuite()

        test_suite.addTest(RanzhiTest("test_01_add_user"))
        current = time.strftime("%Y%m%d %H_%M_%S")

        report_path = "D:\\Py\\ranzhi\\reports\\ranzhi_test_report_%s.html" % current
        report_file = open(report_path,mode="wb")

        test_runner = HTMLTestRunner(stream=report_file,
                                     title="Ranzhi自动化报告",
                                     description="后台测试详情")
        test_runner = HTMLTestRunner()

        test_runner.run(test_suite)
        report_file.close()

