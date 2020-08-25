# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/25  10:37
# @abstract    :

import pandas as pd


df = pd.read_excel("./1.xlsx")

print(df.head())

means = df.mean()
data = pd.DataFrame(means).T
print(data)

data.to_excel("./2.xlsx", index=None)
print("ok!")

