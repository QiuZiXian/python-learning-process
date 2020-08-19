# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/18  21:23
# @abstract    :

import math

# 不考虑内存及数据量
# a每行数据以单tab分隔
with open("./a.txt", "r", encoding="utf-8") as f:
	data = f.readlines()


# def test():
# 	pass
#
def calculateAvg(data, sep=","):
	if not data:
		return "输入为空"
	# data必然不为空
	if isinstance(data,list):
		if isinstance(data[0], list):  # data若为嵌套list，返回错误
			return "输入异常==》 只接收单层list"
		for item in data:
			if not str(item) or str(item).isspace(): # 处理空行或空白值
				return ""
			if not str(item).isdigit(): # 是否每行都为数值
				return "数据异常==>数据不全都是数值"

		return sum(data) /len(data)
	if isinstance(data, str):
		try:
			# 递归函数记得return，否则经过这里的calcuteAvg的返回值都是None
			return calculateAvg([int(item.strip("\n")) for item in data.split(sep)])
		except:
			return "数据异常==》 单行内分隔符错误或未统一"

avgs = [str(calculateAvg(item)) + "\n" for item in data]

with open("./b.txt", "w", encoding="utf-8") as f:
	f.writelines(avgs) # 不是逐行写入，即不是一个row一行


# s = "abc"
#
# li = [1, 2]
#
# print(type(s))
# print(type(li))
# print(isinstance(s,tuple))
# print(isinstance(s,str))
# print(isinstance(li,tuple))
