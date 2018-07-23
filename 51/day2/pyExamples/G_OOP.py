# -*- coding: utf-8 -*-
#面向对象编程(Object orient programing)的三大特性：封装、继承、多态
#class：类
#1:构造函数的作用； 2：变量类型的作用域（成员变量、私有变量(局部变量)）
class Person(object):
    age=0           #类中的成员变量，也叫属性
    weight=0
    def __init__(self, n, w=8):   #构造函数，起到实例化的时候预设一些值或其他操作
        self.name = n    #加上self的变量也是成员变量，但n是私有变量
        self.weight = w #私有变量只在本函数内部有效，成员变量整个类有效
        self.say()          #函数中调用其他成员函数，要加上self
    def say(self):  #成员函数 也叫方法
        print("出生的第一句话：我叫%s,我刚出生%d岁,重%s斤"
              %(self.name, self.age, self.weight))#引用类成员变量都要加self
if __name__ == '__main__':
    p = Person("张三", 30) #类需要实例化才能使用，实例化同时执行构造函数（如果有参数要传参给构造函数）
    l = Person("李四", 40)
    p.say()                        #又调用了say函数
    print(p.name)                  #调用类中的姓名