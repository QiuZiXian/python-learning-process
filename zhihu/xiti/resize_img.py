# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/31  15:33
# @abstract    :  question: 循环放在函数内部还是函数外部

import os
from PIL import Image

def getImgs(filePath): # 遍历文件夹获取 所有图片
	imgs = []
	for parent, paths, files in os.walk(filePath):
		for file in files:
			fileName, ext = os.path.splitext(file)
			if ext in ['jpg', 'png', 'gif', 'jpeg']:
				imgs.append(file)
				# imgs.append(os.path.join(parent, file))
		break # 当前路径


def filterImgs(imgs, dpi): # 过滤图片，获取大于分辨率的图片
	newImgs = []
	for item in imgs:
		im = Image.open(item)
		if max(im.size()) > dpi:
			newImgs.append(item)
	return newImgs

def resizeImg(filePath, img, dpi):
	fileName, ext = os.path

	im = Image.open(img)
	x, y = im.size()
	if x >= y :
		resizeRate = x/dpi
		new = int(y/resizeRate)
		newIm = im.resize((dpi,new))
	else:
		resizeRate = y/dpi
		new = int(x/resizeRate)
		newIm = im.resize((new,x))
	newIm.save()

