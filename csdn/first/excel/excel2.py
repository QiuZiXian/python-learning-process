# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/16  9:05
# @abstract    :


# import pandas as pd
#
#
# df_day = pd.read_excel("D:/d/python/auto/csdn1.xlsx", index_col=0) # 每天的excel
# df_report = pd.read_excel("D:/d/python/auto/csdn2.xlsx", index_col=0) # 待插入汇报excel
#
# for row in df_day.index.values:
# 	for col in list(df_day):
# 		try:
# 			df_report.at[row, col] = df_day.at[row, col]
# 		except:
# 			print("找不到对应数据， 坐标", row, ",", col)
#
# df_report.fillna(0)
# df_report["合计"] = df_report.apply(lambda col:col.sum(), axis=1)
# df_report.loc["合计"] = df_report.apply(lambda col:col.sum())
#
# print(df_report)
#
# df_report.to_excel("D:/d/python/auto/csdn2.xlsx") # 输出处理好的汇报excel
#
# print("ok!")



import pandas as pd


df = pd.read_excel("D:/d/python/auto/csdn1.xlsx", index_col=0)
indexList = [3, 2]  # 选取的索引列表

print(df)
# df.loc[indexList].to_excel("D:/d/python/auto/csdn3.xlsx")



