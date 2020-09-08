# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/31  13:13
# @abstract    :

import random
from matplotlib import pyplot as plt
from PIL import Image

# 定义热图的横纵坐标
xLabel = ['A', 'B', 'C']
yLabel = ['1', '2', '3']

# 准备数据阶段，利用random生成二维数据（5*5）
data = []
for i in range(3):
	temp = []
	for j in range(3):
		k = random.randint(0, 100)
		temp.append(k)
	data.append(temp)

# 作图阶段
fig = plt.figure()
# 定义画布为1*1个划分，并在第1个位置上进行作图
ax = fig.add_subplot(111)
# 定义横纵坐标的刻度
ax.set_yticks(range(len(yLabel)))
ax.set_yticklabels(yLabel)
ax.set_xticks(range(len(xLabel)))
ax.set_xticklabels(xLabel)
# 作图并选择热图的颜色填充风格，这里选择hot
image = Image.open('./1.png')
print(type(image))
print(image)
im = ax.imshow(image, cmap=plt.cm.hot_r)
# 增加右侧的颜色刻度条
plt.colorbar(im)
# 增加标题
plt.title("test")
# show
plt.show()
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties

# font = FontProperties(fname='/Library/Fonts/Songti.ttc')


def draw():
	# 定义热图的横纵坐标
	xLabel = ['A', 'B', 'C']
	yLabel = ['1', '2', '3']

	# 准备数据阶段，利用random生成二维数据（5*5）
	data = []
	for i in range(3):
		temp = []
		for j in range(3):
			k = random.randint(0, 100)
			temp.append(k)
		data.append(temp)

	# 作图阶段
	fig = plt.figure()
	# 定义画布为1*1个划分，并在第1个位置上进行作图
	ax = fig.add_subplot(111)
	# 定义横纵坐标的刻度
	ax.set_yticks(range(len(yLabel)))
	ax.set_yticklabels(yLabel)
	ax.set_xticks(range(len(xLabel)))
	ax.set_xticklabels(xLabel)
	# 作图并选择热图的颜色填充风格，这里选择hot
	im = ax.imshow(data, cmap=plt.cm.hot_r)
	# 增加右侧的颜色刻度条
	plt.colorbar(im)
	# 增加标题
	plt.title("This is a title")
	# show
	plt.show()


# d = draw()