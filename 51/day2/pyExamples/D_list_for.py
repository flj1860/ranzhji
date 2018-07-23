# -*- coding: utf-8 -*-
#数组又叫列表（list）：分为一维数组、二维数组、多维数组，第五种变量
#一维数组： 将一串变量或值合并到一个数组变量中，如下：
fruits1 = ["banana", "apple", "mango", "berry"]
fruits2 = ["banana", 10, 6.5]

#二维数组：将一维数组又组成一个一维数组，如下：
fruits3 = [["banana", 10, 6.5], ["apple", 5, 8], ["mango", 2, 9], ["berry", 8, 20.5]]
#把上面的二维数组列成表格：
"""
品名     数量  单价
"banaba" 10   6.5
"apple"  5    8
"mango"  2    9
"berry"  8    20.5
"""
#读取数组中的元素，可以用下标直接获取，下标从0开始计数
print("我今天吃了好多%s。"%fruits1[3])
#二维数组的下标有行和列：fruits3[行号][列号]
# + - * /  :加减乘除
mSum = fruits3[0][1] * fruits3[0][2]        # 10（第1行第2列） * 6.5（第1行第3列）
print("我今天买了%d斤%s,单价是%.2f一斤，总共花了%.2f元人民币"
      %(fruits3[0][1], fruits3[0][0], fruits3[0][2], mSum))

#循环语句：for 变量 in 集合
#意思就是说在某一个集合中循环取值赋给 变量 ，直到值被取完
for j in "hello 你好 python! ":
    print(j)
#下面开始循环一维数组,依次输出所有水果名称
for fruit in fruits1:
    print(fruit)                    #这里输出的是一个一个的水果名称
#下面开始循环二维数组,依次输出所有水果名称以及信息
for fruit in fruits3:
    print(fruit)                    #这里输出的是水果的一维数组
#按照下列方式打印数据：
"""
banana
10
6.5
apple
.......
"""
#下面开始两层循环嵌套，遍历二维数组里面的每一个元素
for fruit in fruits3:           #循环行
    for f in fruit:             #循环当前行的每一列
        print(f)                #打印每一行的每一列元素

