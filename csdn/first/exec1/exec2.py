# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/5  15:55
# @abstract    :


import os
import sys


all = []


global c,i


input("欢迎使用程序，输入quit以退出，录入数据格式：如：男\n1心仪女1，则输入：男1 = 女1，按下回车继续...")


while True:
    a = []
    expression = input("请录入数据：")
    if expression == "quit":
        for i in all:
            a = i
            b = a
            c = exec(f"{b} = None")
            d = all[c]
            o = b
            exec(f"v = \"{b}\"")
            if v == o:
                print(f"{o}和{v}配对成功")
    else:
        expression = expression.strip()
        expression.replace('=','=')
        a = expression.split('=')
        b = a[0]
        c = a[1]
        z = str(c)
        all.append(exec(f'{b} = "{c}"'))