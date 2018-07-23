# -*- coding: utf-8 -*-
'''知识点：

'''
import time
from selenium import webdriver              #导入webdriver功能库
from selenium.webdriver.support.select import Select    #导入Select类，用来操作列表元素

f = webdriver.FirefoxProfile("firefoxpro")  #加载火狐的配置信息
b = webdriver.Firefox(f)                      #打开一个空白的火狐
b.implicitly_wait(10)                         #隐式等待10秒，直到一个页面被完全加载
b.get("http://localhost:8090/ranzhi/www") #打开然之首页
#find_element_by_name
elem = b.find_element_by_name("account")    #用那么属性找到用户名输入框，并赋值给elem变量
elem.send_keys("abcdef")  #输入错误的用户名
time.sleep(2)
elem.clear()                #清除原内容
#find_element_by_class_name
b.find_element_by_class_name("form-control").send_keys("admin") #如果有多个满足条件，默认返回第一个(用户名输入框)，输入正确的用户名
#find_elements_by_class_name
elems = b.find_elements_by_class_name("form-control") #find_elements，这里返回一个元素数组（两个）
elems[1].send_keys("111111") #数组中第二个是密码输入框，输入密码
#find_elements_by_tag_name
tags = b.find_elements_by_tag_name("input")         #查找页面中所有的input元素
#从tags列表的五个元素中找出submit按钮
#元素变量.get_attribute("属性名") ：在一个元素上获取指定属性名的属性值
for t in tags:
    if t.get_attribute("value") == "登录":    #如果当前这个元素的value值是 登录 表示它是登录按钮
        t.click()
        break                                  #找到了就点击并中断循环
time.sleep(2)
#接下来在登陆成功页面点击“客户管理”图标按钮
#2345浏览器--F12--找到你要定位元素HTML代码处--右键--copy--xpath， 得到下面的定位串
b.find_element_by_xpath('//*[@id="s-menu-1"]/button').click()
#b.find_element_by_xpath('/html/body/div/div[1]/div/ul[1]/li[1]/button')   #这个也可以，但是不稳定
#先切换到CRM内容所在的iFrame中去
b.switch_to.frame("iframe-1")   #第一种:如果iframe有ID
#f = b.get_element_by_xxx("iframe节点属性")   #第二种：如果iframe没有ID，可以先定位到这个iframe节点
#b.switch_to.frame(f)              # 然后切换到这个iframe节点
#find_element_by_link_text：根据超链的文字定位
b.find_element_by_link_text("产品").click()               #点击 产品 超链
#点击 “添加产品”
#find_element_by_partial_link_text：根据超链的部分文字定位
b.find_element_by_partial_link_text("加产").click()               #点击 添加产品 超链
time.sleep(2)
#下面开始添加产品信息
b.find_element_by_id("name").send_keys("2018自动化产品")
#选择产品线
listE = b.find_element_by_id("line")
selE = Select(listE)
selE.select_by_index(1)                     #选择根据索引顺序
selE.select_by_value("ee")                  #选择根据列表值
selE.select_by_visible_text("51测试产品线")#选择根据列表的可见文字
#选择类型
listE = b.find_element_by_id("type")
selE = Select(listE)
selE.select_by_visible_text("服务类")                     #选择根据列表的可见文字
#选择状态
listE = b.find_element_by_id("status")
selE = Select(listE)
selE.select_by_visible_text("正常")                     #选择根据列表的可见文字
b.find_element_by_id("submit").click()                  #点击保存
time.sleep(2)
#接下来验证一下产品有没有出现在列表的第一行
#节点.text: 获取指定节点下的所有文字内容
#用css_selector定位表格中第一行的产品名称
pName1 = b.find_element_by_css_selector("#productList > tbody > tr:nth-child(1) > td.text-left").text
#用xpath定位表格中第一行的产品名称
pName2 = b.find_element_by_xpath("//table[@id='productList']/tbody/tr[1]/td[2]").text
if pName1 == "2018自动化产品":
    print("添加成功")
else:
    print("添加失败")