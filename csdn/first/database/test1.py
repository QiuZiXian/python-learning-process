# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/29  21:50
# @abstract    :

from itertools import combinations

li = [num for num in range(1, 33)]


# i = 0
# for item in combinations(li,9):
# 	print(item)
# 	i += 1
# 	if i > 100:
# 		break



import numpy as np

theta = np.zeros((3,1))
b2 = np.array([1])

# print(theta.shape)
# # print(np.zeros([3,1]))
#
# theta2 = np.zeros([3,1])
# print(theta2.shape)

print(theta)
print(b2)
# print(theta@b2)


def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der

print(rosen_der(np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])))

# if np.array([1, 2, 3, 4, 5]):
# 	print("ok")