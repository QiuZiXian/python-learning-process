# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/23  13:14
# @abstract    :	鼠标点击画布，出现万花筒


# 导入相关类库
import turtle as t
import random as r

# 左转的角度列表 提供给下面的程序使用
a = [68, 92, 125, 140, 144]
# 设置背景色为黑色
t.bgcolor("black")
# 设置画笔速度
t.speed(100)


def goto(x, y):
    # 移动画笔到 (x,y)
    t.goto(x, y)


def cursorx_y(event):  # 光标x，y的移动,event事件
    # 鼠标单击事件发生的对象 里面有单击时候的坐标
    # 下面的绘画的 x y坐标
    # 运行下面的运算之后 图形不会出现在鼠标下面
    x = event.x - 380
    y = 330 - event.y
    # 抬笔
    t.penup()
    # 移动画笔
    goto(x, y)
    # 画图形
    huatuxing()


def huatuxing(event):
    # 抬笔
    t.penup()
    # 产生-350-350之间的随机数 大概是屏幕的左右中间位置
    x = r.randint(-350, 350)
    # 产生-250, 250之间的随机数 大概是屏幕的上下中间位置
    y = r.randint(-250, 250)
    # 移动画笔到 (x, y)
    t.goto(x, y)
    # 设置画笔的 颜色 为随机颜色
    t.color(r.random(), r.random(), r.random())
    # 落笔
    t.pendown()
    # 取一个随机的旋转角度
    ra = a[r.randint(0, 4)]

    # 设置画笔长度为40-80之间的随机数
    for i in range(r.randint(40, 80)):
        # 向前画
        t.fd(i)
        # 左转 ra 角度
        t.left(ra)


huihua = t.getscreen()  # 意思为返回一个Turtle Screen类的绘图对象，并开启绘画
# 设置画布宽高
t.setup(600, 600)
# 移动鼠标
# t.onclick(goto)
huihua.cv.bind("<Button-1>", huatuxing)  # 绑定鼠标左键

# 结束绘画
t.done()