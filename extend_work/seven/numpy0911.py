# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/11  14:02
# @abstract    :
import ctypes
import numpy as np
from ctypes import *
# DAQdll   = ctypes.WinDLL("USB5000.dll")
# DAQdll = ctypes.CDLL("USB5000.dll")
DAQdll = windll.LoadLibrary('USB5000.dll')
ADCvalue = (c_float*3000)()
DAQdll.USB5GetAi(0, 1000, byref(ADCvalue), 1)  ## 将采集的数据传给 ADCvalue
# ADC      = np.ctypeslib.as_array(ADCvalue )    ## 转为numpy数组
ADC      = np.array(ADCvalue )    ## 转为numpy数组
print(ADC[100])                                ## OK， 单个数值可以正确输出
print(ADC[:100])                               ## 有问题，数组不能打印出来
np.savetxt("task2.txt", ADC , fmt="%f", delimiter=" ")  ## 出错！！！

with open('task2.npy', 'wb') as f:
    np.save(f, ADC)
