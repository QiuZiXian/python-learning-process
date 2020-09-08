# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/30  21:59
# @abstract    :

import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts
# import execjs

# 准备数据
provinces = ['北京', '上海', '黑龙江', '吉林', '辽宁', '内蒙古', '新疆', '西藏', '青海', '四川', '云南', '陕西', '重庆',
			 '贵州', '广西', '海南', '澳门', '湖南', '江西', '福建', '安徽', '浙江', '江苏', '宁夏', '山西', '河北', '天津']

num = [1, 1, 1, 17, 9, 22, 23, 42, 35, 7, 20, 21, 16, 24, 16, 21, 37, 12, 13, 14, 13, 7, 22, 8, 16, 13, 13]

color_series = ['#FAE927', '#E9E416', '#C9DA36', '#9ECB3C', '#6DBC49',
				'#37B44E', '#3DBA78', '#14ADCF', '#209AC9', '#1E91CA',
				'#2C6BA0', '#2B55A1', '#2D3D8E', '#44388E', '#6A368B',
				'#7D3990', '#A63F98', '#C31C88', '#D52178', '#D5225B',
				'#D02C2A', '#D44C2D', '#F57A34', '#FA8F2F', '#D99D21',
				'#CF7B25', '#CF7B25', '#CF7B25']

# 创建数据框
df = pd.DataFrame({'provinces': provinces, 'num': num})
# 降序排序
df.sort_values(by='num', ascending=False, inplace=True)

# 提取数据
v = df['provinces'].values.tolist()  # 省s
d = df['num'].values.tolist()  # 数量

# 制作玫瑰图
(
	Pie(init_opts=opts.InitOpts(width='1350px', height='750px', bg_color='silver'))  # 生成一个饼图对象,初始化绘图区域
	.add("", [list(z) for z in zip(v, d)], center=["50%", "65%"], radius=["30%", "135%"], rosetype="area")  # 添加数据，定义玫瑰图类型
	# .add("", ["多地确诊病例连续多日零新增"], pos="center", is_label_show=True, label_text_color=None, is_random=True)
	.set_colors(color_series)  # 设置颜色
	# 设置全局配置项
	.set_global_opts(title_opts=opts.TitleOpts(title='多地确诊病例连续多日零新增', pos_left="40%", pos_top="60%"),
					 legend_opts=opts.LegendOpts(is_show=False),
					 toolbox_opts=opts.ToolboxOpts())
	# 设置序列（花瓣）配置项
	.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
											   formatter="{b}:{c}天", font_style="italic", font_weight="bold", font_family="Microsoft YaHei")
					 )

	# 输出 html文档
	.render('南丁格尔玫瑰图-精简.html')
)