# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/16  21:05
# @abstract    :  头像添加未读消息数


from PIL import Image, ImageDraw, ImageFont, ImageFilter

import os

# print (os.getcwd())

# def add_num(img):
#     draw = ImageDraw.Draw(img)
#     myfont = ImageFont.truetype('d:/d/python/font/Arial.ttf', size=40)
#     fillcolor = "#ff0000"
#     width, height = img.size
#     draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
#     img.save('01.jpg','jpeg')
#
#     return 0
# if __name__ == '__main__':
#     image = Image.open('00.jpg')
#     add_num(image)

# image = Image.open('00.jpg') # 打开图片
# w, h = image.size	# 获取图片的宽高



# draw = ImageDraw.Draw(image) # 把图片放在画布上
#
# font = ImageFont.truetype('arial.ttf', 50) # 设置字体、大小
# draw.text((4 * w / 5, h / 5), '5', fill=(255, 10, 10), font=font) # text((x, y), content, fontColor, font)
# image.save('01.png', 'png')

# 图片 操作： 打开、保存； 放大、缩小、切片、旋转、滤镜、模糊效果、 添加文字、调色板等
im = Image.open('test.jpg') # 打开一个jpg图像文件
w, h = im.size


im.thumbnail((w/2, h/2)) # 获得图像尺寸
im.save('thumbnail.jpg', 'jpeg') # 保存文件，主要文件后缀，jpg

im.filter(ImageFilter.BLUR) # 模糊效果
im.save('blur.jpg', 'jpeg')




