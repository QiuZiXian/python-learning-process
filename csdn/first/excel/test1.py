# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/31  17:16
# @abstract    :

import pandas as pd


df = pd.DataFrame([[1, 2, 3], [2, 2, 2]])
row = df.iloc[0:2]
newDf = pd.DataFrame()
newDf = newDf.append([row] * 5)
print(newDf)