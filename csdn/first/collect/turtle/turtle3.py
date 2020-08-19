# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/16  12:25
# @abstract    :

import turtle

import random

turtle.bgcolor("black")      # 设置颜色

turtle.speed(0)

def cursor_x_y(event):

   x = event.x - 300

   y = 300-event.y

   turtle.penup()

   num=random.randint(1,3)

   if(num==1):

        goto(x,y)

        draw()

   elif(num==2):

       draw_star(x,y)

   else:

       draw_circle(x,y)



def draw_circle(x,y):

   turtle.penup()

   turtle.goto(x,y)

   turtle.pendown()

   turtle.circle(random.randint(10,50))





def draw_star(x,y):

   turtle.begin_fill()

   sides = 5

   length = random.randint(10,50)

   angle = 720.0 / sides

   turtle.penup()

   turtle.goto(x,y)

   turtle.pendown()

   for i in range(sides):

           turtle.forward(length)

           turtle.right(angle)

   turtle.end_fill()

def goto(x,y):

   turtle.goto(x,y)

def draw():

   for j in range(1):

       turtle.penup()

       goto(random.randint(-300,300),random.randint(-300,300))

       turtle.pendown()

       turtle.color(random.random(),random.random(),random.random())

       arg = random.randint(20,80)

       turtle.seth(arg)

       for i in range(random.randint(10,50)):

           turtle.fd(i)

           turtle.left(90)



   turtle.ht()





scr = turtle.getscreen()

scr.setup(600,600)

#scr.onclick(goto)

scr.cv.bind("<Button-1>",cursor_x_y)

#draw()