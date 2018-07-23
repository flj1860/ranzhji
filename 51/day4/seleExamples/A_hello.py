# -*- coding: utf-8 -*-
import time
from selenium import webdriver              #导入webdriver功能库

#    去掉firefox的各种插件及关闭各种更新
#    将下面的文件夹拷贝到项目文件夹下：
#    win7:  C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\XXXX.default"
#    winXP: "c:\document and setting\网管\application data\Mozilla\Firefox\Profiles\XXXX.default"
#    这个文件夹是firefox的配置项存放目录，创建firefox时指定加载这个配置信息
#    如果不指定配置文件夹，系统将按照火狐默认配置加载
f = webdriver.FirefoxProfile("firefoxpro")  #加载火狐的配置信息
b = webdriver.Firefox(f)                      #打开一个空白的火狐
b.get("https://www.baidu.com")            #打开百度页面

elem = b.find_element_by_id("kw")           #根据id=kw来定位百度输入框，找到后赋值给elem变量
elem.send_keys("selenium")                  #往文本输入框输入内容：selenium
elem = b.find_element_by_id("su")              #找到id=su的百度一下按钮
elem.click()                                  #点击按钮
time.sleep(5)                                 #暂停5秒钟
b.save_screenshot("c:\\seleniumScreenshot.jpg")
b.close()           #关闭当前浏览器页面
#b.quit()            #关闭浏览器