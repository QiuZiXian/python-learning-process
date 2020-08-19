# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/12  20:07
# @abstract    : sklearn 的数据集分割

import numpy as np
import random, math

from sklearn.model_selection import train_test_split


# N = int(input("please input N(>0 and even):"))
N = 60

less10 = [(random.randint(0, 10), 0) for i in range(0, int(N/2))]
more10 = [(random.randint(11,100), 1) for i in range(0, int(N/2))]
less10.extend(more10)
tmp = np.array(less10)
mid = np.random.randint(0, 100, (int(N), 3))
a = np.insert(mid, 0, values=tmp[:,0], axis=1)
data = np.c_[a, tmp[:, 1]]
np.random.shuffle(data)
print(data)
print(data.shape)

xTrain, xTest, yTrain, yTest = train_test_split(data[:,0:3], data[:,4], test_size=0.2, random_state=0)
print(xTrain)
print(xTest)
print(yTrain)
print(yTest)
# firstCol = np.array([0]*N)

# from random import  random, randrange,randint, uniform
#
#
# print(random())
# # print(randint(2, math.inf))
# print(randrange(3))
# print(uniform(3, math.inf))