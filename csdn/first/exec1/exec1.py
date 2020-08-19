# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/5  15:27
# @abstract    :


import os
import sys
# all = {}
# global c, i
# input("欢迎使用程序，输入quit以退出，录入数据格式：如：男\n1心仪女1，则输入：男1 = 女1，按下回车继续...")
# key = 1
# while True:
#     a = []
#     expression = input("请录入数据：")
#     if expression == "quit":
#         for i in all:
#             # exec('b=all[i]')
#             b = all[i]
#             if b in all:
#                 if i == all[b]:
#                     print(i+'和'+b+'配对成功')
#                     all[b] = 'NONE'
#         break
#     else:
#         expression = expression.strip()
#         expression.replace('=', '=')
#         a = expression.split('=')
#         b = a[0]
#         c = a[1]
#         all[b] = c
#         # exec(f'all[b] = c')



'''
1. 录入数据，数据格式为男1 = 女1
2. 结束并输出，结束标志位quit
'''

print("=================================================")
print("欢迎使用程序，输入quit以退出，录入数据格式：如：\n男1心仪女1，则输入：男1 = 女1，按下回车继续...\n")
print("===========================================")

data = {}


def getData(rawData):  # 获取数据 函数
    if "=" not in rawData: # 简单数据格式判断
        print("请确认输入格式！")
        return
    tmp = rawData.split("=")
    data[tmp[0].strip()] = tmp[-1].strip()


def outAndPring(data): # 退出并输出结果
    success = []
    for key,value in data.items():
        value2 = data.get(value)
        if value2:
            if key not in success: # 避免重复，男1=女1 女1=男1 只需要输出一次
                if key == value2:
                    print(f'{key}和{value}配对成功')
                    success.append(value)

while True:
    rawData = input("请录入数据：")
    if rawData.strip() == "quit": # 如果遇到quit则退出程序并输出结果
        outAndPring(data)
        break
    else:
        getData(rawData) # 接收数据并处理