# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/15  21:24
# @abstract    :


import turtle

import random

turtle.bgcolor("black")      # 设置 画板颜色，即背景色

turtle.speed(0) # 画笔速度



for j in range(100):

   turtle.penup() # 提笔

   # turtle.goto(random.randint(-300, 300), random.randint(-300, 300))   # 这样随机面积更大
   #


   turtle.goto(random.randint(1,300),random.randint(1,300)) # goto(a, b) 笔尖落点坐标（a, b）

   turtle.pendown() # 落笔

   turtle.color(random.random(),random.random(),random.random()) # color(r, g, b) 画笔颜色，三原色

   arg = random.randint(20,80) # 随机角度值

   turtle.seth(arg) #  画笔转角角度

   for i in range(random.randint(10,50)):



       turtle.fd(i)

       turtle.left(90) # 左转90度


# 按上述设置开始 作画
turtle.done()

