# -*- coding: utf-8 -*-
#import ：导入
import os    #这里实际上是导入了os.py, os：operating system:操作系统
import time  #这里导入了time.py
import F_function   #导入自己写的F-function.py文件,import实际上会执行这个文件
from pyExamples.F_function import *
from pyExamples.G_OOP import Person

print(os.getcwd())      #获取当前文件所在的路径
print(os.getenv("path"))#获取windows环境变量path的内容

print(time.ctime())     #打印当前的时间
print(time.strftime("%Y-%m-%d %H:%M:%S %a"))

F_function.add(19, 20)          #输出39
print(sub(40, 20))
x = Person("王五",50)
