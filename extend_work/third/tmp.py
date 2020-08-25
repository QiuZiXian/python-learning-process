# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/24  21:55
# @abstract    :

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import xlrd
x_data = []
y_data1 = []
y_data2 = []
y_data3 = []
y_data4 = []

data = xlrd.open_workbook(r'E:\data\txt\d01.xlsx')
table = data.sheets()[0]

cap = table.col_values(0)
for j in range(1, 461):
    x_data.append(cap[j])
print(cap)

cap1 = table.col_values(1)
print(cap1)  #打印出来检验是否正确读取
for i in range(1, 461):
    y_data1.append(cap1[i])

cap2 = table.col_values(2)
print(cap2)  #打印出来检验是否正确读取
for i in range(1, 461):
    y_data2.append(cap1[i])

cap3 = table.col_values(3)
print(cap3)  #打印出来检验是否正确读取
for i in range(1, 461):
    y_data3.append(cap1[i])

cap4 = table.col_values(4)
print(cap4)  #打印出来检验是否正确读取
for i in range(1, 461):
    y_data4.append(cap1[i])

ln1,=plt.plot(x_data, y_data1, color='red', linewidth=1.5, marker='v')
ln2,=plt.plot(x_data, y_data2, color='dodgerblue', linewidth=1.5, marker='*')
ln3,=plt.plot(x_data, y_data3, color='springgreen', linewidth=1.5, marker='X')
ln4,=plt.plot(x_data, y_data4, color='magenta', linewidth=1.5, marker='d')

plt.legend(['0','60°','90°','120°'],loc='upper right')

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 15,
         }
plt.xlabel('wavelength $\lambda$($\mu$m)',font1)
plt.ylabel('Exitinction effciency factor $Q_{ext}$',font1)
plt.show()