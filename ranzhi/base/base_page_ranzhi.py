#coding=utf-8
from selenium import webdriver

from base.automate_driver import AutomateDriver


class BasePage():
    def setUp(self):
        self.driver = AutomateDriver()
        self.driver.implicitly_wait(5)
        self.driver.navigate('localhost:803/ranzhi/www')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit_browser()
