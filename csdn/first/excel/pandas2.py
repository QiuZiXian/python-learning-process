# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/29  18:46
# @abstract    :

import pandas as pd

df = pd.date_range('2020-07-29 00:00:00', '2020-07-30 00:00:00', freq= '5min')
print(df)