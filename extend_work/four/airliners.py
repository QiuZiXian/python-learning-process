# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/27  23:05
# @abstract    :

class Airliner:
	type: str	# 客机类型
	aluminium_alloy: float	# 铝合金
	titanium_alloy: float	# 钛合金
	magnesium_alloy: float	# 镁合金
	panel: float	# 板材
	templet: float	# 型板
	tubular_product: float	# 管材
	plastic: float	# 塑料

	def __init__(self, type, aluminium_alloy,titanium_alloy, magnesium_alloy, panel, templet, tubular_product,plastic):
		self.type = type
		self.aluminium_alloy = aluminium_alloy
		self.titanium_alloy = titanium_alloy
		self.magnesium_alloy = magnesium_alloy
		self.panel = panel
		self.templet = templet
		self.tubular_product = tubular_product
		self.plastic = plastic

	def __add__(self, other):
		return Airliner(self.type,
						self.aluminium_alloy + other.aluminium_alloy,
						self.titanium_alloy + other.titanium_alloy,
						self.magnesium_alloy + other.magnesium_alloy,
						self.panel + other.panel,
						self.templet + other.templet,
						self.tubular_product + other.tubular_product,
						self.plastic + other.plastic)

	def __str__(self):
		return "\n Airliner type: " + self.type + \
			"\n aluminium_alloy:" + '{:f}'.format(self.aluminium_alloy) + "ton" \
			"\n titanium_alloy:" + '{:f}'.format(self.titanium_alloy) + "ton" \
			"\n magnesium_alloy" + '{:f}'.format(self.magnesium_alloy) + "ton" \
			"\n panel" + '{:f}'.format(self.panel) + "ton" + \
			"\n templet:" + '{:f}'.format(self.templet) + "ton" \
			"\n tubular_product:" + '{:f}'.format(self.tubular_product) + "ton" \
			"\n plastic" + '{:f}'.format(self.plastic) + "kg"

class Subsonic_Airliner(Airliner):
	country: str
	engines: int

	def __init__(self, type, aluminium_alloy, titanium_alloy, magnesium_alloy, panel, templet, tubular_product, plastic, country, engines):
		super().__init__(type, aluminium_alloy, titanium_alloy, magnesium_alloy, panel, templet, tubular_product, plastic)

		self.country = country
		self.engines = engines

class Supersonic_Airliner(Airliner):
	country: str
	engines: int

	def __init__(self, type, aluminium_alloy, titanium_alloy, magnesium_alloy, panel, templet, tubular_product, plastic, country, engines):
		super().__init__(type, aluminium_alloy, titanium_alloy, magnesium_alloy, panel, templet, tubular_product, plastic)

		self.country = country
		self.engines = engines

class Hypersonic_Airliner(Airliner):
	country: str
	engines: int

	def __init__(self, type, aluminium_alloy, titanium_alloy, magnesium_alloy, panel, templet, tubular_product, plastic, country, engines):
		super().__init__(type, aluminium_alloy, titanium_alloy, magnesium_alloy, panel, templet, tubular_product, plastic)

		self.country = country
		self.engines = engines



if __name__ == '__main__':
	airliners = []
	airliners.append(Subsonic_Airliner("Boeing_trump", 9, 9, 9, 9, 77, 88, 99, "USA", 1))
	airliners.append(Supersonic_Airliner("Mitsubishi_SpaceJet", 3, 4, 2, 3, 75, 88, 99, "Poland", 2))
	airliners.append(Hypersonic_Airliner("Comac_C919", 3, 4, 2, 3, 75, 88, 99, "China", 4))
	total = Airliner("total", 0, 0, 0, 0, 0, 0, 0)
	for airliner in airliners:
		assert isinstance(total, object)
		total += airliner
		print(str(airliner))
	print("================================")
	print(total.type, ':', total.titanium_alloy, 'ton')
	print(total)

