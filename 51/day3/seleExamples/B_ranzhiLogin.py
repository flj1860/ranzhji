# -*- coding: utf-8 -*-
'''知识点：
    1、browser.implicitly_wait() 隐式等待以替换time.sleep(n)；
    2、隐式等待会出现失效(偏差)情况，需要结合sleep函数使用；
    3、通常情况下自动化测试需要验证之前的操作是否成功，此处采用验证浏览器标题以判断是否登录成功。
'''
import time
from selenium import webdriver              #导入webdriver功能库

f = webdriver.FirefoxProfile("firefoxpro")  #加载火狐的配置信息
b = webdriver.Firefox(f)                      #打开一个空白的火狐
b.implicitly_wait(10)                         #隐式等待10秒，直到一个页面被完全加载
b.get("http://localhost:8090/ranzhi/www") #打开然之首页

b.find_element_by_id("account").send_keys("admin")  #输入用户名
b.find_element_by_id("password").send_keys("111111")#输入密码
b.find_element_by_id("submit").click()               #点击登录
#使用页面标题判断一下是否登录成功
time.sleep(2)  #由于页面标题的改变是JS完成的，隐式等待无法识别，因此要人为等待2秒
if b.title == "然之协同":                           #判断当前浏览器标题是否是期望值
    print("登录成功")
else:
    print("登录失败")
