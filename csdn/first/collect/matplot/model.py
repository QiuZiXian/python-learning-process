# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 01:56:48 2020

@author: 87875
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(130, 190, 1)
print(len(x))
y = 97.928 * np.exp(- np.exp(-  0.1416 *( x - 146.1 )))
z = 96.9684 * np.exp(- np.exp(-0.1530*( x - 144.4)))
z2 = 94.9684 * np.exp(- np.exp(-0.1330*( x - 141.4)))

print(y, z, z2)
print(type(y))
# =============================================================================
# fig, ax = plt.subplots()
# line1, = ax.plot(x, y, color = "r")
# line2, = ax.plot(x, z, color = "g")
# line3, = ax.plot(x, z, color = "b")
# 
# def update(num, x, y, z,z2, line1, line2, line3):
#     line1.set_data(x[:num], y[:num])
#     line2.set_data(x[:num], z[:num])
#     line3.set_data(x[:num], z2[:num])
#     return [line1,line2,line3]
# 
# ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, z,z2, line1, line2, line3],
#                   interval=200, blit=True)
# 
# ax.set_xlabel('Age (day)')
# ax.set_ylabel('EO (%)')
# 
# plt.show()
# =============================================================================

