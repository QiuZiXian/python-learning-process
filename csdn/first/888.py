# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:55:48 2020

@author: 87875
"""
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random 

# fake data
frame_num = 100
gps_data = [-104 - (4 * random.rand(2, frame_num)), 31 + (3 * random.rand(2, frame_num))]


fig = plt.figure()
ax1 = plt.axes(xlim=(-108, -104), ylim=(31,34))
line, = ax1.plot([], [], lw=2)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plotlays, plotcols = [2], ["black","red"]
lines = []
for index in range(2):
    lobj = ax1.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
    return lines

x1,y1 = [],[]
x2,y2 = [],[]

frame_num = len(gps_data[0])

# animation function.  This is called sequentially
def animate(i):

    x = gps_data[0][i,3]
    y = gps_data[0][i,2]
    x1.append(x)
    y1.append(y)

    x = gps_data[1][i,3]
    y = gps_data[1][i,2]
    x2.append(x)
    y2.append(y)

    #X = np.array(x1, x2)
    #Y = np.array(y1, y2)

    #for index in range(0,1):
    for lnum,line in enumerate(lines):
        line.set_data([x1,y1, x2,y2])
    return lines,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=1, blit=True)


plt.show()