# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/24  21:06
# @abstract    :



filename = 'G1.txt'  # 数据路径

with open(filename, 'r', encoding='utf-8') as f:
	lines = f.readlines()

data_dict = {}
for line in lines:
	item = line.strip('\n').split(" ")
	if len(item) != 4:
		print(item)
		continue
	key = int(item[0][1:])
	n = int(item[0][1:])
	x = float(item[1][1:])
	y = float(item[2][1:])
	z = float(item[3][1:])

	if key not in data_dict:
		data_dict[key] = [(n, x, y, z)]
	else:
		data_dict[key].append((n, x, y, z))



print("========================处理后的数据========================")
data_dict2 = {}
for group in [1, 2, 3, 4]:
	data = []
	for i in range(1 + 18*(group -1), 10 + 18*(group - 1)):
		item = data_dict[i]
		if i % 2 == 0:
			item.reverse()
			data.append(item)
		else:
			data.append(item)
	for i in range(18*group, 9 + 18*(group - 1), -1):
		item = data_dict[i]
		if i % 2 == 0:
			item.reverse()
			data.append(item)
		else:
			data.append(item)
	data_dict2[group] = data

for group in [1, 2, 3, 4]:
	print("第", group, "组数据：", len(data_dict2[group]))
	for item in data_dict2[group]:
		for dots in item:
			print(dots)
