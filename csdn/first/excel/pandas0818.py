# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/18  12:17
# @abstract    :


import pandas as pd

# df = pd.read_excel("./11.xls")
#
# groups = df.groupby("客户").sum()
# print(groups)
#
# groups.to_excel('./22.xls')


data = pd.read_excel("./11.xls", sheet_name="Sheet2")
out = data[[data.columns[0], data.columns[1]]]
for i in range(1, int(len(data.columns) / 2)):
    new = data[[data.columns[2 * i], data.columns[2 * i + 1]]]
    out = pd.merge(out,
                   new,
                   left_on=data.columns[2 * i - 2],
                   right_on=data.columns[2 * i],
                   how='inner')
out.to_excel('结果.xls',index=None)