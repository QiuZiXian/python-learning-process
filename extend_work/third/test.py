# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/24  21:31
# @abstract    :

li = [1, 3, 7, 5, 2, 6]

print(li)
# li.reverse()
li = li[::-1]
print(li)

print(li[0:2])


for i in range(10, 0, -1):
	print(i)

import torch
from matplotlib import image