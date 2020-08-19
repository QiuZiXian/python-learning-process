# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/2  16:22
# @abstract    :


# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
#-----底图绘制
matplotlib.rcParams['toolbar'] = 'None'
fig = plt.figure(figsize=(8, 8), edgecolor='w')
m = Basemap(
            width = 60000,
            height = 60000,
            projection='tmerc',
            #llcrnrlon=116.55,#起始经度116
            llcrnrlat=40.3, #起始纬度
            #urcrnrlon=116.80, #终止经度117
            urcrnrlat=40.9,#终止纬度41
            lon_0 = 116.66,
            lat_0 = 40.52,
            resolution='c',
            )
island_col = '#FFDEAD' #陆地颜色
line_col = 'purple' #轨迹颜色
m.drawmapboundary(fill_color = 'aqua')
m.fillcontinents(color = island_col,lake_color = 'white')
m.drawparallels(np.arange(24,41,0.05),labels=[1,1,0,0])
m.drawmeridians(np.arange(112,120,0.15),labels=[0,0,0,1])

shp_info = m.readshapefile("D:/d/python/python/shape_eg_data/mexico/cities",'counties')#D:/d/python/python/shape_eg_data_mexico/mexico

#-----数据读取
# posi = pd.read_csv('first_car.csv',header = 0, names = ['name','lng','lat'])
# num = len(posi)
# lng = posi["lng"].values # 获取经度值
# lat = posi["lat"].values # 获取纬度值
# x,y = m(lng,lat)
# #-----轨迹绘制
# m.scatter(x, y, s=1, c='r', alpha=0.7, zorder=10)
#m.plot(x,y,marker=None,color = line_col,linewidth = 1)
plt.show()

# plt.figure(figsize=(4,4))
# m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=100)
# m.bluemarble(scale=0.5)


# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# # setup Lambert Conformal basemap.
# # set resolution=None to skip processing of boundary datasets.
# m = Basemap(width=12000000,height=9000000,projection='lcc',
#             resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
# m.bluemarble()
# plt.show()
# plt.show()