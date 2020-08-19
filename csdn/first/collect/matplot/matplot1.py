# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/31  19:30
# @abstract    :

# =============================================================================
# import spidev
# =============================================================================

import time

import argparse

import sys

# import navio.mpu9250FIFO

# =============================================================================
# import navio.util
# =============================================================================

from matplotlib import pyplot as plt

import matplotlib.animation as animation

import numpy as np

# from math import *
#
# import matplotlib as mpl
#
# import platform

# =============================================================================
# navio.util.check_apm()
# 
# imu = navio.mpu9250FIFO.MPU9250(0, 0)
# 
# if imu.testConnection():
# 
# 	print("Connection established: True")
# 
# else:
# 
# 	sys.exit("Connection established: False")
# 
# imu.initialize()
# 
# time.sleep(1)
# 
# imu.enableFIFO(True, 'acc')
# =============================================================================

# ---Draw---

# fig, ax = plt.subplots()

fig = plt.figure(num='PMC_ACC_PLOT', figsize=(5, 4))

ax = fig.add_subplot(1, 1, 1)

ax.set_title('PMC Accelerometer')

ax.set_xlabel("Count")

ax.set_ylabel("Accelerometer Output")



ax.set_ylim(20, -20)

# 这是第一条
xdata, ydata = [0] * 100, [0] * 100
line, = ax.plot(np.random.rand(100), 'g')
def update(data):
	line.set_ydata(data)

	return line,


def run(data):
	global xdata, ydata

	x, y = data

	if (x == 0):
		xdata = [0] * 1000

		ydata = [0] * 1000

	del xdata[0]

	del ydata[0]

	xdata.append(x)

	ydata.append(y)

	line.set_data(xdata, ydata)

	return line,


def data_gen():
	x = 99

	while True:

		if (x >= 99):

			x = 0

		else:

			x += 0.1

		try:

			imu.read_acc()

			m9a = imu.accelerometer_data

			print("Acc:", "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2]))

			inRaw = m9a[0]

			inInt = float(inRaw)



		except:

			inInt = 0

		yield x, inInt


ani = animation.FuncAnimation(fig, run, data_gen, interval=0, blit=True)
# 这是第二条
# =============================================================================
# xdata, ydata = [0] * 100, [0] * 100
# line2, = ax.plot(np.random.rand(100), 'g')
# def update2(data):
# 	line2.set_ydata(data)
# 
# 	return line2,
# 
# 
# def run2(data):
# 	global xdata, ydata
# 
# 	x, y = data
# 
# 	if (x == 0):
# 		xdata = [0] * 1000
# 
# 		ydata = [0] * 1000
# 
# 	del xdata[0]
# 
# 	del ydata[0]
# 
# 	xdata.append(x)
# 
# 	ydata.append(y)
# 
# 	line2.set_data(xdata, ydata)
# 
# 	return line2,
# 
# 
# def data_gen2():
# 	x = 99
# 
# 	while True:
# 
# 		if (x >= 99):
# 
# 			x = 0
# 
# 		else:
# 
# 			x += 0.1
# 
# 		try:
# 
# 			imu.read_acc()
# 
# 			m9a = imu.accelerometer_data
# 
# 			print("Acc:", "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2]))
# 
# 			inRaw = m9a[0]
# 
# 			inInt = float(inRaw)
# 
# 
# 
# 		except:
# 
# 			inInt = 0
# 
# 		yield x, inInt
# 
# 
# ani = animation.FuncAnimation(fig, run2, data_gen2, interval=0, blit=True)
# # 这是第三条
# xdata, ydata = [0] * 100, [0] * 100
# line3, = ax.plot(np.random.rand(100), 'g')
# def update3(data):
# 	line3.set_ydata(data)
# 
# 	return line3,
# 
# 
# def run3(data):
# 	global xdata, ydata
# 
# 	x, y = data
# 
# 	if (x == 0):
# 		xdata = [0] * 1000
# 
# 		ydata = [0] * 1000
# 
# 	del xdata[0]
# 
# 	del ydata[0]
# 
# 	xdata.append(x)
# 
# 	ydata.append(y)
# 
# 	line3.set_data(xdata, ydata)
# 
# 	return line3,
# 
# 
# def data_gen3():
# 	x = 99
# 
# 	while True:
# 
# 		if (x >= 99):
# 
# 			x = 0
# 
# 		else:
# 
# 			x += 0.1
# 
# 		try:
# 
# 			imu.read_acc()
# 
# 			m9a = imu.accelerometer_data
# 
# 			print("Acc:", "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2]))
# 
# 			inRaw = m9a[0]
# 
# 			inInt = float(inRaw)
# 
# 
# 
# 		except:
# 
# 			inInt = 0
# 
# 		yield x, inInt
# 
# 
# ani = animation.FuncAnimation(fig, run3, data_gen3, interval=0, blit=True)
# =============================================================================

plt.show()