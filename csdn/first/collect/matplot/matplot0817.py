# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/18  19:18
# @abstract    :

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

plt.rcParams['xtick.direction'] = 'in'#将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内

plt.xlim(3,5)
plt.ylim(2,3.5) # y轴范围

x_data = [3.0000, 3.2222, 3.4444, 3.6667, 3.8889, 4.1111, 4.3333, 4.5556, 4.7778, 5.0000]
y_data = [2.2637, 2.4006, 2.4239, 2.4727, 2.4676, 2.4688, 2.4829, 2.4287, 2.3771, 2.2745]
y_data2 = [2.4953, 2.6352, 2.6272, 2.6342, 2.5806, 2.5433, 2.5187, 2.4156, 2.3203, 2.1917]
y_data3 = [2.7354, 2.9002, 2.8853, 2.8840, 2.8204, 2.7748, 2.7358, 2.5965, 2.4583, 2.2855]
y_data4 = [2.7875 ,2.9530 ,2.9319 ,2.9227 ,2.8521 ,2.8000 ,2.7539 ,2.6076 ,2.4629 ,2.2845]
y_data5 = [2.9395 ,3.1134 ,3.0779 ,3.0430 ,2.9414 ,2.8555 ,2.7706 ,2.5897 ,2.4290 ,2.2456]

ln1, = plt.plot(x_data, y_data, color='red', linewidth=2.0, marker='v')
ln2, = plt.plot(x_data, y_data2, color='dodgerblue', linewidth=2.0, marker='*')
ln3, = plt.plot(x_data, y_data3, color='springgreen', linewidth=2.0, marker='p')
ln4, = plt.plot(x_data, y_data4, color='cyan', linewidth=2.0, marker='H')
ln5, = plt.plot(x_data, y_data5, color='magenta', linewidth=2.0, marker='d')

plt.legend(['sphere','ellipsoid','cylinder','rhabditiform','chain'],loc='upper right') #设置图例，loc设置图例位置

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 15,
         }
plt.xlabel('wave length$\lambda$($\mu$m)',font1) # 希腊字母
plt.ylabel('$Q_{ext}$',font1) # 带下标的变量

plt.show()