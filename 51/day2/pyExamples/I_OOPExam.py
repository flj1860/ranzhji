# -*- coding: utf-8 -*-
#创建一个Siri类,继承自G_OOP.Person
#该类应该具备构造函数，直接指定姓名，体重，年龄，爱好
#添加方法：getName，getAge ,getFavor
#添加方法: setName
from pyExamples.G_OOP import Person #从J_OO.py中导入Person类
class siri(Person):         #siri继承了Person类，也就得到了Person的所有成员变量以及函数
    def __init__(self, name, weight, age, favor):   #重写了父类的构造函数，多态的一种
        Person.__init__(self,name,weight)    #调用父类的构造函数
        self.age = age                  #相比父类的构造函数又增加了内容
        self.favor = favor
    def getName(self):
        print("我叫%s"%self.name)
    def getAge(self):
        print("我今年%d了"%self.age)
    def getFavor(self):
        print("我的爱好是%s" % self.favor)
    def setName(self, name):            #给siri改名
        self.name = name
        print("我现在改名叫%s" % self.name)
if __name__ == '__main__':
    s = siri("siri", 10, 5, "吃饭、睡觉、打豆豆...")
    s.say()     #再说一次出生语
    while True:
        x = input("请问你有什么问题吗?")
        if "姓名" in x:  # if 如果，如果在用户的提问中包含 "姓名" 两个字
            s.getName()
        elif "年龄" in x:  # elif 否则如果包含“年龄”
            s.getAge()
        elif "爱好" in x:  # 否则如果包含“爱好”
            s.getFavor()
        elif "改名" in x:
            y = input("你觉得叫什么好?")
            s.setName(y)
        elif "bye" in x:
            break
        else:  # 当前面的都没有满足，则执行这个
            print("你好，我好像没有听明白，能重复一遍吗？")

