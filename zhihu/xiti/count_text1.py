# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/30  17:22
# @abstract    :

with open("count.txt","r", encoding="utf-8") as f:
	content = f.read()
# print(content)
contentList = content.split(" ")

countDict = {}
for item in contentList:
	key = item.strip("\n").rstrip(".")
	if key in countDict:
		countDict[key] += 1
	else:
		countDict[key] = 1

for key,value in countDict.items():
	print(key, value)
