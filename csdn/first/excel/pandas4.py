# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/31  16:43
# @abstract    :
import random
import pandas as pd
import numpy as np

# def getSample(length):
# 	"""
# 	随机生成length长度的列表
# 	来源：大小写、数字
# 	:param length: 选取长度
# 	:return: sample为list
# 	"""
# 	alnum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# 	sample = random.sample(alnum, length)
#
# 	return sample
# c = ["".join(getSample(10)) for i in range(2000)]
# d = [i for i in range(2000)]
# new = np.array([c]).reshape(2000, 1)
# newd = np.array([d]).reshape(2000, 1)
# data = np.hstack((new, newd))
# # print(data)
# df = pd.DataFrame(data,columns=["商品名称", "类别"])
# df.to_csv("product.csv", sep=",", index=None)

df = pd.read_csv("product.csv", sep=",")

rows = df.iloc[0:2001]
# newDf = pd.DataFrame()
data = [rows]*2
print(data)
# data = np.array(data)
# np.random.shuffle(data)
# print(data.shape)
# print(data)
# newDf = pd.DataFrame(data, columns=["商品名称", "类别"])
# newDf.to_csv("agent.csv", sep=",",index=None)
print("ok!")

