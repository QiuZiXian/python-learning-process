# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/6  9:29
# @abstract    :



filepath = "./data.txt" # the full pathname of your data file
with open(filepath, "r", encoding="utf-8") as f: # get data
	data = f.readlines()
# handle data
myList = []
for item in data[1:]:
	if "#" in item:
		print(myList)
		myList = []
		continue
	myList.append(item.strip("\n"))

# if the number of the separator (#) is all the same
# it's easy to handle your problem by the faction of "split" like below

# filepath = "./data.txt" # the full pathname of your data file
# with open(filepath, "r", encoding="utf-8") as f: # get data
# 	# f.readline()  # fiter the first line
# 	data = f.read()
# data = data.strip("#").strip("\n").split("###########################\n")
# for item in data:
# 	print(item.split("\n"))