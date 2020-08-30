# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/28  11:16
# @abstract    :

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# #fig = plt.figure(figsize=(12, 8))
# #ax = Axes3D(fig)
# #delta = 0.125
# X = np.array([3.0000, 3.2222, 3.4444, 3.6667, 3.8889, 4.1111, 4.3333, 4.5556, 4.7778, 5.0000])
# Y = np.array([1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4])
# X, Y = np.meshgrid(X, Y)
# print("网格化后的X=",Y)
# print("X维度信息",Y.shape)
# print("网格化后的Y=",Y)
# print("Y维度信息", Y.shape)
# Z = np.array(
#     [
#     [2.6530, 2.7425, 2.8191, 2.8837, 2.9395, 2.7322, 3.0390, 3.0839, 3.1258],
#     [2.7726, 2.8781, 2.9694, 3.0479, 3.1134, 2.7403, 3.2164, 3.2619, 3.3044],
#     [2.6863, 2.8023, 2.9071, 2.9985, 3.0779, 2.7483, 3.2020, 3.2506, 3.2957],
#     [2.6006, 2.7220, 2.8408, 2.9487, 3.0430, 2.7563, 3.1975, 3.2581, 3.3093],
#     [2.4758, 2.5960, 2.7156, 2.8334, 2.9414, 2.7643, 3.1198, 3.1935, 3.2571],
#     [2.3669, 2.5012, 2.6196, 2.7382, 2.8555, 2.7724, 3.0589, 3.1426, 3.2171],
#     [2.2395, 2.3967, 2.5305, 2.6500, 2.7706, 2.7804, 3.0006, 3.0980, 3.1831],
#     [2.0241, 2.1856, 2.3393, 2.4710, 2.5897, 2.7884, 2.8319, 2.9456, 3.0472],
#     [1.8285, 1.9860, 2.1457, 2.2981, 2.4290, 2.7964, 2.6703, 2.7944, 2.9121],
#     [1.6465, 1.7957, 1.9459, 2.0993, 2.2456, 2.8045, 2.4877, 2.6073, 2.7302]
#     ]
# )
# print("维度调整前的Z轴数据维度",Z.shape)
# Z = Z.T
# print("维度调整后的Z轴数据维度",Z.shape)
# # 绘制三维曲面图
# surf=ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# #设置三个坐标轴信息
# font1 = {'family': 'Times New Roman',
#          'weight': 'normal',
#          'size': 15,
#          }
# ax.set_xlabel('wavelength $\lambda$($\mu$m)', color='b')
# ax.set_ylabel('partical size($\mu$m)', color='g')
# ax.set_zlabel('Exitinction effciency factor $Q{_ext}$', color='r')
# plt.tick_params(labelsize=12)
# labels = ax.get_xticklabels() + ax.get_yticklabels()+ ax.get_zticklabels()
# [label.set_fontname('Times New Roman') for label in labels]
#
# fig.colorbar(surf, shrink=0.5, aspect=8)

def example_surface(ax):
    """ draw an example surface. code borrowed from http://matplotlib.org/examples/mplot3d/surface3d_demo.html """
    from matplotlib import cm
    import numpy as np
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)


plt.draw()
plt.show()