# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/27  9:17
# @abstract    :

import pandas as pd
# # use_cols = ["C", "B"]
# #
# # df = pd.read_csv("data.csv", usecols=use_cols)
# # filtered_df = df.dropna()
# # print(filtered_df.tail())
# # df.B.isin(["value"])
# #
# # chunkSize = 1000000
# # data_iterator = pd.read_csv("data.csv",usecols=use_cols, chunksize=chunkSize)
# #
# # use_cols = ["C", "B"]
# # chunks = [data_chunk for data_chunk in data_iterator]
# # df = pd.concat(chunks, ignore_index=True)
# # df.B.isin(["value"])
# #
# # df2 = df.drop(['B', 'C'], axis=1) # 按列名过滤列
# #
# # df.groupby
#
# import numpy as np
#
#
# df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
#                        ('bird', 'Psittaciformes', 24.0),
#                        ('mammal', 'Carnivora', 80.2),
#                        ('mammal', 'Primates', np.nan),
#                       ('mammal', 'Carnivora', 58)],
#                      index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
#                       columns=('class', 'order', 'max_speed'))
#
# df.a=df.a.astype("int")
# print(df.groupby('class'))
# for name,group in df.groupby('class'):
# 	print(name)
# 	print(group)
# use_cols = ["A", "B""C"]
df = pd.read_csv("data.csv", header=1, encoding="gbk", index_col=0)
print(df)
grouped = df.groupby('组序号')
dList =[]
for a, b in grouped:
	# if b["组员名录"].isnall
    if b["组员名录"].isin(b["组长"]).any():
        bList = b.shape[0]*[1]
    else:
        bList = b.shape[0] * [0]
    dList.extend(bList)
    print(bList)
df["判断值"] = dList
df.to_csv("out.csv",sep=",")
print(df)

# import pandas as pd
# import numpy as np
#
#
# df = pd.read_excel("111.xls")
# a,b = df.shape
#
# for index,row in df.iterrows():  # （第一步） ，取出每一个样本
#     rowList = list(row.values) * 64
#     arrays = np.array(rowList).reshape((32, 32)) # 第二步 ， 样本数据填充成 32*32
#     np.random.shuffle(arrays) # 打乱32*32矩阵数据
#     rowArrays = np.vstack((arrays, arrays, arrays)) # 第三步， 生成三通道
#     print(rowArrays)








# import pandas as pd
#
#
# data = pd.read_csv('data.csv',header=None, encoding="gbk")
# data = data.loc[1:,1:]
# top = bottom = 1
# flag =0
# now = data.loc[1,2]
# for i in range(1,len(data.loc[:,1])+1):
#     if (i+1 > len(data.loc[:,2])) or now != data.loc[i+1,3]:
#         top = i
#         if flag == 1:
#             data.loc[bottom:top,4] = 1
#             flag = 0
#         else:
#             data.loc[bottom:top,4] = 0
#         bottom = top +1
#         if i+1 < len(data.loc[:,2]):
#             now = data.loc[i+1,3]
#     if data.loc[i,2] == data.loc[i,3]:
#         flag = 1
# print(data)
# data.to_csv('123.csv',header=None)



