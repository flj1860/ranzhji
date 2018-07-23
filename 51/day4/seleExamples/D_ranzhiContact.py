# -*- coding: utf-8 -*-
import time
from selenium import webdriver              #导入webdriver功能库
from selenium.webdriver.common.keys import Keys #导入所有按键

f = webdriver.FirefoxProfile("firefoxpro")  #加载火狐的配置信息
b = webdriver.Firefox(f)                      #打开一个空白的火狐
b.implicitly_wait(10)                         #隐式等待10秒，直到一个页面被完全加载
b.get("http://localhost:8090/ranzhi/www") #打开然之首页

b.find_element_by_id("account").send_keys("admin")  #输入用户名
b.find_element_by_id("password").send_keys("111111")#输入密码
b.find_element_by_id("submit").click()               #点击登录
time.sleep(2)

#接下来在登陆成功页面点击“客户管理”图标按钮
b.find_element_by_xpath('//*[@id="s-menu-1"]/button').click()
#先切换到CRM内容所在的iFrame中去
b.switch_to.frame("iframe-1")   #第一种:如果iframe有ID
#点击联系人
b.find_element_by_link_text("联系人").click()
#点击添加联系人
b.find_element_by_link_text("添加联系人").click()
#真实姓名
b.find_element_by_id("realname").send_keys("吴大伟")
#决策人
ckb = b.find_element_by_id("maker")
if ckb.is_selected() == False:  #如果决策人复选框没有被选中，则点击选中
    ckb.click()
#所属客户，需要先点击下拉框，再在下拉的div中的input输入框中输入内容，再回车
b.find_element_by_id("customer_chosen").click()
b.find_element_by_css_selector("div[class='chosen-search'] > input").send_keys("国防科大" + Keys.ENTER)
#性别
b.find_element_by_id("gender1")
#简介
b.find_element_by_id("desc").send_keys("是一个好人！")
#保存
b.find_element_by_id("submit").click()
time.sleep(2)
#继续保存
try:
    b.find_element_by_id("continueSubmit").click()
except:
    pass
#验证一下第一行姓名是否正确
if b.find_element_by_xpath("//table[@id='contactList']/tbody/tr[1]/td[2]").text == "吴大伟":
    print("添加成功")
else:
    print("添加失败")
#将该数据删除
b.find_element_by_link_text("更多").click()#点击界面上 第一个 更多
time.sleep(1)
b.find_element_by_link_text("删除").click()
time.sleep(2)
at = b.switch_to.alert    #得到JS消息框
print("消息框的内容:%s"%at.text)
at.accept() #点击确定
#at.dismiss() #点击取消
b.close()# 关闭浏览器

