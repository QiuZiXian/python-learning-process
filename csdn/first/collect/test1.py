# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/15  21:40
# @abstract    :

# a1=[[0]*2]*2
# a2=[[0,0],[0,0]]
#
# # a1=[[0]*2]*2
# # a2=[[0,0],[0,0]]
# a1[0][0]=1
# a2[0][0]=1
#
# print(a1)
# print(a2)
#
#
# print(id(a1[0]))
# print(id(a1[1]))
# print(id(a2[0]))
# print(id(a2[1]))


# a = b = 0 #
#
# print(a, b)
# print(id(a))
# print(id(b))
# b = 10
#
# print(id(a))
# print(id(b))

a = None  # 可以使用==； 也可以直接作为真假值进行判断

# if not	a:
# 	print("test")

if a == None:
	print("test")

#############################################
# x = int(input('请输入整数：'))
# if x % 2 == 0:
#     a = (2+x)*(x/2)/2
#     print('1~'+str(x)+'奇数合='+str(a-x/2)+',偶数合='+str(a))
# else:
#     b = x-1
#     a = (2+b)*(b/2)/2
#     print('1~'+str(x)+'奇数合='+str(a-b/2+x)+',偶数合='+str(a))


###############################################
a = [0, 0, 0]
b = c = 0
d = '一二三'
for i in range(3):
    a[i] = float(input('请输入第'+d[i]+'个实数：'))
    b += a[i]
    c += a[i]/3
print('合计为{:.1f},平均为{:.1f}'.format(b, c))