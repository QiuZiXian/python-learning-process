# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/12  19:31
# @abstract    :

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv("1.csv",encoding = "gbk",engine = "python",sep = "\t")
df.index = df["update_time"]
# print(df)

df.index = pd.to_datetime(df.index)#将index类型转换为 datetime 时间序列。，否则无法进行下一行的 index.day
df["day"] = df.index.day
df["period"] = pd.cut(df["day"],[4,10,11,14],labels = ['双11前','双11当天','双11后'])
df["period"] = pd.cut(df["day"],np.array([4,10,11,14]),labels = ['双11前','双11当天','双11后'])
df21 = df[["price","item","period"]].groupby(["item","price"]).min()
df21.reset_index(inplace = True)
price = df21["item"].value_counts()
id_count1 = price[price == 1].index
id_count2 = price[price != 1].index


df22 = df[["item","price","day","店名"]]
df22x = df22.groupby(["item","price"]).min()
df22x.reset_index(inplace = True)
pre11_price = df22x[df22x["day"] <= 11]
late11_price = df22x[df22x["day"] == 11]

tot11_price = pd.merge(pre11_price,late11_price,on = "item")

tot11_price["zkl"] = (tot11_price["price_x"] - tot11_price["price_y"]) / tot11_price["price_x"]
final11 = tot11_price[["item","店名_x","zkl"]]
final11["zkl_range"] = pd.cut(final11["zkl"],bins = np.linspace(0,1,21), labels=[i for i in "abcdefghijklmnopqrst"])
print(final11["zkl_range"])
final11["zkl_range"]=final11["zkl_range"].tolist()
bokedata = final11.groupby(["zkl_range"]).count().iloc[:-1]
print(bokedata.head())
bokedata.reset_index(inplace = True)
bokedata["per"] = bokedata["zkl"] / bokedata["zkl"].sum()

from bokeh.io import output_notebook,output_file
from bokeh.plotting import figure,show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
output_file("heihei.html")
#json.dumps(bokedata["zkl_range"],cls=MyEncoder,indent=4)

src = ColumnDataSource(bokedata)

lstzkl = bokedata.index.tolist()
hover = HoverTool(tooltips = [("折扣率","@zkl")])
bokedata.index = bokedata.index.tolist()
print(bokedata["item"])
p = figure(x_range=(-420, 420), plot_width= 900,plot_height = 350,title = "折扣率分布图",
           tools = [hover,'reset,xwheel_zoom,pan,crosshair'])
p.line(x = "zkl_range",y = "per",source = src , line_color = "blue")
p.circle(x = "zkl_range",y = "per",source = src ,color = "red",size = 8)

# print(bokedata["zkl_range"])
# print(bokedata["per"])
# p.line(x = bokedata["zkl_range"].tolist(),y = bokedata["per"], line_color = "blue")
# p.circle(x = bokedata["zkl_range"].tolist(),y = bokedata["per"],color = "red",size = 8)

show(p)