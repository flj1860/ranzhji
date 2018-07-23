# -*- coding: utf-8 -*-
#软件开发模式：面向过程、面向对象
#下面定义两个函数，def--define：定义
#函数（function,意思是将一个功能封装为一个函数）
#函数说明：输入两个任意数字，输出相加的结果
# 输入参数：x: 任意数字；y：任意数字
# 输出参数：None，打印输出x+y结果到屏幕

def add(x, y):
    z = x + y
    print(z)
#函数说明：输入两个任意数字，返回相减的结果给调用者
# 输入参数：x: 任意数字；y：任意数字，默认值为0.0
# 输出参数：x - y结果返回给调用者
def sub(x, y=0):
    z = x - y
    return z     #返回z的值给调用者，return将结束函数的运行
#__name__：变量 ，当当前py文件是主入口执行文件的时候，等于__main__
#否则当被其他py文件import的时候，等于所在文件的文件名
if __name__ == '__main__':
    add(10,20)
    x = add(20,30)
    y = sub(30,20)
    m = sub(30)
    n = sub(y=10, x=20)
    print("x|y|m|n : %r|%r|%r|%r"%(x,y,m,n))
    print("认识一下print",end="，你好！\n")
