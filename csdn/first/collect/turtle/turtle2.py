# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/15  21:48
# @abstract    :

import turtle

numbers = [1,11,10,20,21,12,22]



x=100

r=20

for num in numbers:

   x=x+10

   if(num <=10):

           turtle.penup()

           turtle.goto(x,100)

           turtle.pd()

           turtle.begin_fill()

           turtle.pencolor('red')

           turtle.fillcolor('red')

           turtle.circle(r)

           turtle.end_fill()

   elif(num > 10 and num <= 20):

           turtle.penup()

           turtle.goto(x,100)

           turtle.pd()

           turtle.begin_fill()

           turtle.pencolor('yellow')

           turtle.fillcolor('yellow')

           turtle.circle(r)

           turtle.end_fill()

   elif(num >20 and num <= 30):

           turtle.penup()

           turtle.goto(x,100)

           turtle.pendown()

           turtle.begin_fill()

           turtle.pencolor('blue')

           turtle.fillcolor('blue')

           turtle.circle(r)

           turtle.end_fill()





turtle.ht()