# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/16  21:40
# @abstract    :


# import random


# for num in range(65, 90): # A -Z : 65 - 89
# 	print(chr(num))
# RuntimeError: implement_array_function method already has a docstring

# for num in range(97, 123): # 97 - 122 : a -z
# 	print(chr(num))

#48 - 57

# print("a" + 1) # python 的 字符串 + 数字运算会报错，无法自动转化运算

# s = "Welcome to www.pythonexamples.org. Here, you will find python programs for all general use cases.\
# This is another line with some words."
#
# print(len(s.split())) # 默认空格分隔
#
# import numpy as np
#
# np.reshape

import numpy as np

a1 = np.array([[1,2,3],[4,5,6]])
b1 = np.array([1,2,3])
a2 = np.array([1,2,3])
b2 = np.array([1,2,3])

print(a1*b1)

print(a1 @ b1)