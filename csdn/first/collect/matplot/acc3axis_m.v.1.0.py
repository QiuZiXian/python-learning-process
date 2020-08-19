import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import spidev
import time
import argparse 
import sys
import navio.mpu9250FIFO
import navio.util
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import*
import matplotlib as mpl
import platform
 
navio.util.check_apm()
imu = navio.mpu9250FIFO.MPU9250(0,0)
if imu.testConnection():
    print ("Connection established: True")
else:
    sys.exit("Connection established: False")
imu.initialize()
time.sleep(1)
imu.enableFIFO(True, 'acc')
#--------------------------------------------------

x = np.arange(0, 100, 1)
print(len(x))
imu.read_acc()
m9a = imu.accelerometer_data
print(m9a[0],m9a[1],m9a[2])
'''
y = 97.928 * np.exp(- np.exp(-  0.1416 *( x - 146.1 )))
z = 96.9684 * np.exp(- np.exp(-0.1530*( x - 144.4)))
z2 = 94.9684 * np.exp(- np.exp(-0.1330*( x - 141.4)))
'''
y=m9a[0]
z=m9a[1]
z2=m9a[2]

fig, ax = plt.subplots()
line1, = ax.plot(x, y, color = "r")
line2, = ax.plot(x, z, color = "g")
line3, = ax.plot(x, z2, color = "b")

def update(num, x, y, z,z2, line1, line2, line3):
    imu.read_acc()
    m9a = imu.accelerometer_data
    y=m9a[0]
    z=m9a[1]
    z2=m9a[2]
    line1.set_data(x[:num], y[:num])
    line2.set_data(x[:num], z[:num])
    line3.set_data(x[:num], z2[:num])
    return [line1,line2,line3]

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, z,z2, line1, line2, line3],
                  interval=200, blit=True)

ax.set_xlabel('Age (day)')
ax.set_ylabel('EO (%)')

plt.show()