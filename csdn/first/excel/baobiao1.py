# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/10  9:22
# @abstract    :


import pandas as pd
import os

def isExcel(file):
	if os.path.splitext(file)[-1] in ["xls", "xlsx"]:
		return True
	else:
		return False

def getPathYear(a,item):
	try:
		return (os.path.join(a, item), os.path.splitext(item)[0].strip("代理-"))
	except:
		return []


path = "D:/d"
for a,b,c in os.walk(path):
	filePaths = [getPathYear(item) for item in c if isExcel(item)]
	break

def init(filePaths):
	item = filePaths[0]
	df1 = pd.read_excel(item[0], sheet_name=item[1])
	df2 = pd.read_excel(item[0], sheet_name=item[1] + "-新开")
	df3 = pd.read_excel(item[0], sheet_name=item[1] + "-消费")
	df1.to_excel("zong.xlsx", sheet_name=item[1])
	df1.to_excel("xin.xlsx", sheet_name=item[1] + "-新开")
	df1.to_excel("xiao.xlsx", sheet_name=item[1] + "-消费")

def handle(filePaths):
	for item in filePaths:
		if item	:
			sheetName1 = item[1]
			sheetName2 = item[1] + "-新开"
			sheetName3 = item[1] + "-消费"
			df1 = pd.read_excel(item[0], sheet_name=item[1])
			df2 = pd.read_excel(item[0], sheet_name=sheetName2)
			df3 = pd.read_excel(item[0], sheet_name=sheetName3)

			with pd.ExcelWriter('zong.xlsx', mode='a') as writer:
				df1.to_excel(writer, sheet_name=sheetName1, index=None)
			with pd.ExcelWriter('xin.xlsx', mode='a') as writer:
				df2.to_excel(writer, sheet_name=sheetName2, index=None)
			with pd.ExcelWriter('xiao.xlsx', mode='a') as writer:
				df3.to_excel(writer, sheet_name=sheetName3, index=None)

init(filePaths)
handle(filePaths)
print("ok!")

