# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/8  19:46
# @abstract    :


for i： # 循环 i次
	A = rand([1, 2, 3], 3, 3) # 随机生成矩阵
   value = det(A)
   if value != 0: # 判断det不等于0
	   print(A)



def test(x):
	return x%2


for i in range(100): # 循环100次

	value = test(i)
	if value == 0:
		print(i) # 输出所有的偶数



