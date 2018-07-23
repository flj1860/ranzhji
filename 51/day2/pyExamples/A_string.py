# -*- coding: utf-8 -*-
#这个是单行注释，代码执行时候会忽略注释行
"""
这个是
多行注释
"""
'''
这个也是多行注释
'''
#打印一行字符串到屏幕
print('hello world, 你好， python！')
#什么是变量，以及变量类型
#首先介绍三种类型的变量：
#字符串型(string), 整数型(integer)，浮点型(float)
name = "张三"    #字符串变量要用引号引起来
age = 25
weight = 75.5678
#造句子的两种方式
#1:直接用+号，来拼接字符串
#字符串是不能直接和整数以及浮点数相加，必须要全部转换为字符串
#变量类型转换函数：str(x):将x转换为字符；int(x)：将x转换为整数；float(x)：将x转换为浮点型
str1 = "我是：" + name + ",我今年" + str(age) + "了，我的体重是" + str(weight) + "KG"
print(str1)
#2：使用占位符的方式来拼接字符串
# %s：字符串占位符，执行时后面的字符串变量内容会替代这个占位符
# %d 整数占位符, 后面须对应整形变量
# %f 浮点占位符，后面须对应浮点型变量
#\ :转义符，表示斜杠后面的内容仅仅代表它原始的意思,\n : 换行
str2 = "我是：%s,我今年%d了，\n我的体重是%.3fKG"%(name,age,weight)
print(str2)
#%r : 随机占位符， 万能占位符
print("万能占位符：%r"%age)

#下面学习标准输入函数,input:输入
"""
answer = input("请问你的姓名：")   #x = input(y) ：y：提示信息；x：得到用户的输入
print("哦，你叫：" + answer)
"""
# 模拟苹果的siri的简单回答
myname = 'Siri'
myage = 18
myfavor = "吃饭、喝茶、看电影、旅游..."
x = input("请问你有什么问题吗?")
if "姓名" in x:  # if 如果，如果在用户的提问中包含 "姓名" 两个字
    print("我叫：%s,很高兴认识你!" %myname)
elif "年龄" in x:  # elif 否则如果包含“年龄”
    print("我叫：%s,我今年%d!" % (myname, myage))
elif "爱好" in x:  # 否则如果包含“爱好”
    print("我叫：%s,我今年%d!我喜欢%s" % (myname, myage, myfavor))
else:  # 当前面的都没有满足，则执行这个
    print("你好，我好像没有听明白，能重复一遍吗？")


