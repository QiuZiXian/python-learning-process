# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/9  10:15
# @abstract    :

'''
问题描述：我想制作一副蒙太奇图片，用纯色小像素块填充，并且计算每种颜色块的数量，写入excel表格，求完整代码

需求：像素块为25*25像素大小，图片是2850*2875大小的，也提供了我尝试制作的代码，不过时灵时不灵的



我的尝试思路：以25为步长遍历图片，计算像素块主色调，生成字典，进行统计。类似词频统计的思路，不过报错了，类型不对图片素材资料
'''

import cv2
import os


# 1.用字典存储每一张图及直方图
def build_index():
	print('正在计算各图片直方图')
	readPath = "C:\\A\\save"
	files = os.listdir(readPath)
	dist = {}

	for file in files:
		imgPath = readPath + '\\' + file
		img = cv2.imread(imgPath)
		hist = []

		for i in range(3):
			ht = cv2.calcHist([img], [i], None, [256], [0, 256])
			hist.append(ht)
		dist[file] = hist

	print('各图片直方图计算已完成！')
	return dist


# 2.用相近的图代替原图
def match_replace(dist):
	print('正在替换图片：')
	width, height = 12800, 7200
	image = cv2.imread('v_2.png')

	for i in range(0, height, 25):
		for j in range(0, width, 25):
			img = image[i:i + 25, j:j + 25, 0:3]

			hist = []
			for k in range(3):
				ht = cv2.calcHist([img], [k], None, [256], [0, 256])
				hist.append(ht)

			sim = 0.0
			for key in dist:
				match0 = cv2.compareHist(hist[0], dist[key][0], cv2.HISTCMP_CORREL)
				match1 = cv2.compareHist(hist[1], dist[key][1], cv2.HISTCMP_CORREL)
				match2 = cv2.compareHist(hist[2], dist[key][2], cv2.HISTCMP_CORREL)
				match = match0 + match1 + match2

				if match > sim:
					sim = match
					rename = key
			image[i:i + 25, j:j + 25, 0:3] = cv2.imread('C:\\A\\save\\' + rename)
	cv2.imwrite('v_3.png', image)
	print('图片替换已完成！')


# 3.混合图片
def mix_image():
	print('正在融合图片：')
	image1 = cv2.imread('v_2.png')
	image2 = cv2.imread('v_3.png')
	dst = cv2.addWeighted(image1, 0.2, image2, 0.8, 3)
	cv2.imwrite('v_mix.png', dst)
	print('图片融合已完成！')


if __name__ == "__main__":
	dist = build_index()
	match_replace(dist)
	mix_image()