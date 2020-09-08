# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/3  15:06
# @abstract    :


with open('file.txt', 'r', encoding='utf-8') as f:
	data = f.readlines()

length = 100
fileIndex = int(len(data)/length)


for i in range(1, fileIndex):
	writeData = []
	for item in data[(i - 1)*length :i*length]:
		writeData.append(item)
		writeData.append('\n')
	with open(str(i) + '.txt', 'w', encoding='utf-8') as f:
		f.writelines(writeData)

if len(data) - fileIndex * length > 0:
	for item in data[fileIndex * length:]:
		writeData.append(item)
		writeData.append('\n')
	with open(str(fileIndex) + '.txt', 'w', encoding='utf-8') as f:
		f.writelines(writeData)