# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/31  8:56
# @abstract    :
import scipy.optimize as opt
import  pandas as pd
import numpy as np
def get_Xy(df):#读取特征
#     """
#     use concat to add intersect feature to avoid side effect
#     not efficient for big dataset though
#     """
    ones = pd.DataFrame({'ones': np.ones(len(df))})#ones是m行1列的dataframe
    data = pd.concat([ones, df], axis=1)  # 合并数据，根据列合并 axis = 1的时候，concat就是行对齐，然后将不同列名称的两张表合并 加列
    X = data.iloc[:, :-1]  # 这个操作返回 ndarray,不是矩阵
    X= X.values
    y = data.iloc[:, -1]
    y = y.values.reshape(len(y),1)
    return X,y

data = pd.DataFrame([[1, 2, 3],[1, 2, 3]])
X, y = get_Xy(data)

def sigmoid(z):
    gz = 1/(1+np.exp(-z))
    return gz

theta = np.zeros((3,1))
theta

def computeCost(theta, X, y):
    ''' cost fn is -l(theta) for you to minimize'''
    # your code here  (appro ~ 2 lines)
    #theta = theta.reshape(3,1)
    #y = y.reshape(100,1)
    np.seterr(divide='ignore')
    first = y*np.log(sigmoid(X@theta))
    second = (1-y)*np.log(1 - sigmoid(X@theta))
    costf = -np.sum(first+second) / (len(X))
    return costf
computeCost(theta, X, y)

def gradient(theta, X, y):
    # your code here  (appro ~ 2 lines)﻿
    tmp =  X.T@(sigmoid(X@theta)-y)/len(X)

    return np.array([item[0] for item in tmp])


# print(gradient(theta, X, y))
def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der
def gradientdescent(theta, X, y,alpha,iters):
    theta = theta.reshape(3,1)
    y = y.reshape(2,1)
    temp = np.zeros(theta.shape)
    for i in range(iters):
        temp = theta -(alpha/len(X))*X.T@(sigmoid(X@theta)-y)
        theta = temp
        cost = computeCost(theta, X, y)
    return theta, cost

alpha = 0.003
iters = 200000
g, cost= gradientdescent(theta, X, y,alpha,iters)
# print(g, '\n',cost)

# gradient = gradient(theta, X, y)
# print(gradient)
# print(type(gradient))

res = opt.minimize(fun=computeCost, x0=theta, args=(X, y),method='Newton-CG', jac=gradient)
# 在这里开始就会报错说The truth value of an array with more than one element is ambiguous. Use a.any() or a.all() Numpy对逻辑表达式判别不清楚
print(res)