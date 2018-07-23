# -*- coding: utf-8 -*-
#IF语句, 分支判断语句,完整的语法如下：
"""
elif：else if：否则如果

格式：
if  条件表达式:
    如果上面的条件表达式是成立的则执行这一段代码
    注意：这段代码隶属于if,需要缩进，并且左对齐
elif  条件表达式：
    ......
elif  条件表达式：
    ......
else:
    .....

"""
#判断逻辑值 a 是否为真。 变量类型第四种：bool型，布尔型:真（True） or 假（False）
#bool只有两个取值：True/False
#如果放在IF语句后面，那么什么是真，什么是假？
#真：True;1;200;"abc"
#假：False;0;"";None(相当于JAVA/mysql的Null)
print(True+True+False)    #输出2   ；True=1   False=0

a = "xyz"
if a:
    print("%r是真的！"%a)
else:
    print("%r是假的！"%a)

#例子：提问用户的性别，并做出相应的输出
answer = input("Are you a schoolboy(y/n)?")
if answer: #表示用户有输入
    if answer == 'y':   #假如用户输入的是 y
        boy = True
    elif answer=='n':   #假如用户输入的是 n
        boy = False
    else:               #用户输入了别的字符
        boy = None      #未知

    if boy:
        print("Hello, My dear boy!")
    elif boy == False:
        print("Hello, My dear girl!")
    else:
        print("Your input is invalid!") #invalid:无效的
else:       #假如用户没有输入直接回车
    print("Please input y or n!")

#这里使用逻辑符号：或与非(or/and/not)(JAVA的是||/&&/！),优先级：非 - 与 - 或
#比较符号：> , < , ==,  !=, >=, <=
a = 1 #一个等于是赋值，两个等于是比较
b = 2
c = True
if a==1 and b==2 and c:             #返回真
    print("上面的条件都是对的")
else:
    print("这句不会执行")

if a==1 and (b==3 or c):            #返回真
    print("上面的条件也是对的")
else:
    print("这句不会执行")
if a==1 and (b==3 or not c):        #返回假 b==3 等价于 not b!=3
    print("上面的条件错了")
else:
    print("这句终于执行了")

#例子：足球俱乐部招人要求是:如果男性， 18~30岁，身高>=175cm 或者 如果女性，18~30岁，身高>=170cm
#根据用户输入的个人信息，写出if语句判断此人是否合格
