# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/4  10:35
# @abstract    :

from typing import Any

import numpy

attack_num = 50 #输入合计对空力值

AWACS_flag = 1 # 是否有预警指挥机或预警机参战?无：0，有：1

award_form=numpy.array([[0,0,0,0,0,0,0],

[0,0,0,0,0,0,0],

[0,0,0,0,0,0,1],

[0,0,0,0,1,1,1],

[0,0,0,1,1,1,1],

[0,0,1,1,1,1,1],

[0,1,1,1,1,1,2],

[1,1,1,1,1,2,2],

[1,1,1,1,2,2,2],

[1,1,2,2,2,2,3]])

touzi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



def abscissa(i):#裁决表横坐标

	a=0

	if touzi[i] < 10:

		a=touzi[i]

	else:

		a=9

	return a





def ordinate():#裁决表纵坐标

	c=0

	if attack_num < 11:

		c=0

	elif attack_num < 22:

		c=1

	elif attack_num < 34:

		c=2

	elif attack_num < 45:

		c=3

	elif attack_num < 64:

		c=4

	elif attack_num < 73:

		c=5

	else:

		c=6

	return c


expection = 0#初始化期望值为0图片捕获.PNG 上传失败图片2.PNG上传失败
for i in range(10):

	touzi[i] += AWACS_flag * 2
	abscissa1 = abscissa(i)  # 获取横坐标
	ordinate1 = ordinate()#获取纵坐标

	result = award_form[abscissa1][ordinate1]#根据(abscissa,ordinate)从award_form裁决表中索引交叉点值

	expection += result/10#expection进行累加

	print("The result is {}".format(result))

print("The expection is {}".format(expection))