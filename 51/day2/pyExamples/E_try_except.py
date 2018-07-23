# -*- coding: utf-8 -*-
#try...except...:错误捕捉语句
#被try包裹的语句如果出现错误，则会跳转到except子句中进行错误处理
try:                        #try:尝试
    print('name')
    x = 1/2
    open("不存在的文件.txt")#上面三行语句都是错误的，只要有一行执行了就会出错，被try捕捉到错误
    print("这句话会不会被执行?")
except Exception as e:                     #except:异常
    print("异常了....")
    print("错误信息:%r"%e)
print("继续运行......")
