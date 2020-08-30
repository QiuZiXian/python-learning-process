# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/27  22:44
# @abstract    :

class airliner:
	type: str	# 类型
	country: str	# 国家
	engines: int	# 引擎
	first_flight: int	# 第一次飞行
	airline_service_entry: int	# 航空公司服务条目
	end_of_production: str	# 生产结束
	number_built: int	# 建造数量
	in_service: int		# 投入使用

	def __add__(self, other):
		return airliner(self.type,
						self.country,
						self.engines + other.engins,
						self.first_flight,
						self.airline_service_entry + other.airline_service_entry,
						self.end_of_production + other.end_of_production,
						self.number_built + self.number_built,
						self.in_service )

	def __str__(self):
		return "\n airliner type:" + self.type +\
			"\n"