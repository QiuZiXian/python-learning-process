# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/7  19:21
# @abstract    :

from pyecharts.charts import Page
Page.save_resize_html("render.html", cfg_file='./chart_config.json', dest="new_charts.html")





# import pyecharts
#
# print(pyecharts.__version__)