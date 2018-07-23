# coding=utf-8

from selenium import webdriver

from function.base.base import Base


class BasePage(object):
    def __init__(self, url):
        self.url = url

    #打开浏览器
    def open_driver(self):
        try:
            fp = webdriver.FirefoxProfile("..\\firefoxpro")
            self.driver = webdriver.Firefox(fp)#打开火狐
            self.driver.maximize_window()#最大化窗口
            self.driver.implicitly_wait(10)      #隐式等待10秒
            self.driver.get(self.url)       #打开首页url
            return True
        except:
            Base.printErr("打开或设置浏览器失败！")
            return False

    #关闭浏览器
    def close_driver(self):
        try:
            self.driver.close()
            return True
        except:
            Base.printErr("浏览器对象不存在！")
            return False
