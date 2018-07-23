# -*- coding: utf-8 -*-
#While循环语句
count = 0
while count < 9:  #当count<9则一直循环
    print('The count is:%d'%count)
    count = count + 1       #变量值累加
print ("Good bye!")

#for循环的写法
#range(9):表示0~8的集合；完整的写法：for count in range(0,9,1): count第一个取0，每循环加1，直到小于9
for count in range(9):
    print('The count is:%d' % count)
print ("Good bye!")

#请判断下面的输出是多少？
#continue: 继续循环 ； break：强制中断循环
i = 94
while i<100:
    i += 1          #等价于 i = i + 1
    if i%2==0:      #%：求余数，2%2=0：2/2等于1余0; 3%2=1,返回的是除法后的余数
        continue    #继续循环，下一句跳转到while i<100，for循环同样适用
    if i>95:
        break       #中断循环，下一句跳出循环语句，for循环同样适用
print(i)

#for循环的写法：
for i in range(94,100,1):
    if i%2==0:      #%：求余数，2%2=0：2/2等于1余0; 3%2=1,返回的是除法后的余数
        continue    #继续循环，下一句跳转到while i<100，for循环同样适用
    if i>95:
        break       #中断循环，下一句跳出循环语句，for循环同样适用
print(i)