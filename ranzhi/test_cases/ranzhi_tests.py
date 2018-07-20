#coding=utf-8
import unittest
import csv
from base.automate_driver import AutomateDriver
from base.base_page_ranzhi import BasePage
from pages.ranzhi_main_page import RanzhiMainPage


class RanzhiTest(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.driver.implicitly_wait(5)
        self.driver.navigate('localhost:803/ranzhi/www')
        self.driver.maximize_window()

    # def tearDown(self):
    #     self.driver.quit_browser()

    def test_01_add_user(self):
        csv_file = open("D:\\Py\\ranzhi\\data\\ranzhi.csv", mode="r", encoding="utf8")
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            login_data = {
                "username":row[0],
                "password":row[1]
            }
            RanzhiMainPage(self.driver).login(login_data)
        #RanzhiMainPage(self.driver).add_user("aaaa","123456")











