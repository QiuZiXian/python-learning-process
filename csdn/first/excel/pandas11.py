# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/11  10:45
# @abstract    :
import pandas as pd

end_data = ['20101011','20110203','20110506','20120608','20130807','20140611']

df = pd.DataFrame(end_data, columns=['time'])

print(df)

print(df['time'].where(df['time'] > '20110611'))
needTimes = df['time'].where(df['time'] > '20110611')

# data2['end_data'].where(data2['end_data'] > '20110611')

# import pandas as pd
# df=pd.DataFrame({"end_data":end_data, "data":[1,2,3,4,5,6]})
# print(df)
# print(pd.date_range("20110406", x["end_data"]))
# is_true = df.apply(lambda x: print(pd.date_range("20110406", x["end_data"])) if len(pd.date_range("20110406", x["end_data"])) else print(pd.date_range("20110406", x["end_data"])), axis=1)
# print(is_true)
# df[is_true]

print(needTimes[3])

timeDf = pd.DataFrame(['2000-12-31 00:00:00', '2019-12-31 00:00:00'], columns=['time'])
timeDf.time = pd.to_datetime(timeDf.time)
# %Y-%m-%d %H:%M:%S
print(timeDf['time'].dt.strftime('%Y%m%d'))

