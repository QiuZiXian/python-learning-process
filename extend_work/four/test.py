# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/28  12:22
# @abstract    :

# print('Exitinction effciency factor $}txe{_Q$'[::-1])


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(plt.figure())
def f(x,y) :
    return -x**2 - y**2

X = np.arange(-1, 1, 0.02)
Y = np.arange(-1, 1, 0.02)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
ax.plot_surface(X, Y, Z, alpha=0.5)

# Hide axes ticks
ax.set_xticks([-1,1])
ax.set_yticks([-1,1])
ax.set_zticks([-2,0])

ax.set_yticklabels([-1,1],rotation=-15, va='center', ha='right')

plt.show()