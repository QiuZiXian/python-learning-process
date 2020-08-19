# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/3  18:17
# @abstract    :
import pandas as pd
import numpy as np


df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                      ('bird', 'Psittaciformes', 24.0),
                       ('mammal', 'Carnivora', 80.2),
                      ('mammal', 'Primates', np.nan),
                      ('mammal', 'Carnivora', 58)],
                     index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                    columns=('class', 'order', 'max_speed'))

print(df)
print(df.groupby('class').groups)


df = pd.read_excel("./test.xlsx", sheet_name=0)