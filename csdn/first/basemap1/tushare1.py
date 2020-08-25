# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/21  21:13
# @abstract    :


# import tushare as ts
#
# ts.set_token('ac2ea413dffff72ddc05ce6bc184a1a13b25c506f85a6447f92ba176')
# pro = ts.pro_api()
#
# # df = ts.pro_bar(ts_code='600588.SH', asset='I', start_date='20190807', end_date='20200807')
# # df = ts.get_hist_data('600588',start='2019-08-07',end='2020-08-07')
# df = pro.daily(ts_code='600588.SH', start_date='20190807', end_date='20200807')
#
# print(df.head())
#
# df.to_csv("./60058SH.csv")

import os


sourcePath = "D:/d/python"
files = os.listdir(sourcePath)
xls_files = [file for file in files if file.endswith(".xls")]
xlsx_files = [file for file in files if file.endswith(".xlsx")]

# 每个xls文件处理
for file in xls_files:
	print(sourcePath + file)

# 每个xlsx文件处理
for file in xlsx_files:
	print(sourcePath + file)
