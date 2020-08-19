# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:14:55 2020

@author: 87875
"""

fig = plt.figure(num='PMC_ACC_PLOT', figsize=(5, 4))

ax = fig.add_subplot(1, 1, 1)

ax.set_title('PMC Accelerometer')

ax.set_xlabel("Count")

ax.set_ylabel("Accelerometer Output")



ax.set_ylim(20, -20)


xdata, ydata = [0] * 100, [0] * 100
xdata2, ydata2 = [0] * 100, [0] * 100
xdata3, ydata3 = [0] * 100, [0] * 100
line, = ax.plot(np.random.rand(100), 'g')
line2, = ax.plot(np.random.rand(100), 'r')
line3, = ax.plot(np.random.rand(100), 'b')


def run(data, xdata, ydata, xdata2, ydata2, xdata3, ydata3, line, line2, line3):
	global xdata, ydata

	x, y = data

	if (x == 0):
		xdata = [0] * 1000

		ydata = [0] * 1000

	del xdata[0]

	del ydata[0]

# 第一条线的变更
	xdata.append(x)
	ydata.append(y)
    
    # 如果更新方法一样直接如下：
    xdata2.append(x)
	ydata2.append(y)
    xdata3.append(x)
	ydata3.append(y)

	line.set_data(xdata, ydata)
    line2.set_data(xdata, ydata)
    line3.set_data(xdata, ydata)

	return [line, line2, line3]


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


ani = animation.FuncAnimation(fig, run, data_gen,fargs=[xdata, ydata, xdata2, ydata2, xdata3, ydata3, line, line2, line3] interval=200, blit=True)
plt.show()