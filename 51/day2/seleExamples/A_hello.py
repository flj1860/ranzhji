# -*- coding: utf-8 -*-

from selenium import webdriver              #导入webdriver功能库
f = webdriver.FirefoxProfile("firefoxpro")
b = webdriver.Firefox(f)                      #打开一个空白的火狐
b.get("https://www.baidu.com")            #打开百度页面

elem = b.find_element_by_id("kw")
elem.send_keys("selenium")
elem = b.find_element_by_id("su")
elem.click()

