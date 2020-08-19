# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/3  19:30
# @abstract    :


import xlwt
import xlrd
import xlutils.copy


# 设置表格样式
def set_style(name, height, bold=False):
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = name
	font.bold = False
	font.color_index = 4
	font.height = height
	style.font = font
	return style


# f = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
# sheet1 = f.add_sheet("大雾", cell_overwrite_ok=True)  # 新建sheet
# f.save(r'D:\d\python\test.xls')  # 保存
Workbook = xlrd.open_workbook('D:/d/python/test.xls')  # 不用\\会报路径错误
sheet2 = Workbook.sheet_by_name('大雾')
workbook_xlutils = xlutils.copy.copy(Workbook)  # 使用xlrd打开一个已存在的xls，并通过xlutils复制
x = int(1)


print(sheet2.name)
print(sheet2.nrows)
print(sheet2.ncols)
# 写Excel
import xarray as xr


def print2excel():
	# lines = open("code.txt", 'r').readlines()
	with open("code.txt", "r") as f:
		lines = f.readlines()
	sheet1 = workbook_xlutils.get_sheet(0)  # 通过sheet序号获取sheet
	x = int(1)
	for i in range(len(lines)):
		if i % 2 == 0:  # 偶数行
			fields = lines[i].strip('\n')
			fields = fields.split(' ')  # split data
			year = fields[0]
			month = fields[1]
			day = fields[2]
			alignment = xlwt.Alignment()
			alignment.horz = xlwt.Alignment.HORZ_CENTER
			alignment.vert = xlwt.Alignment.VERT_CENTER
			sheet1.col(0).width = 256 * 10
			sheet1.col(1).width = 256 * 10
			sheet1.col(2).width = 256 * 10
			sheet1.col(3).width = 256 * 10
			sheet1.col(8).width = 256 * 20
			row0 = ["年", "月", "日", "时次（UTC）", '五角星', '三角', '方框', '黑桃', '备注']
			# 写第一行
			for k in range(0, len(row0)):
				sheet1.write(0, k, row0[k], set_style('Times New Roman', 220, True))
			for j in range(len(fields)):
				int(j)
				n = int(j) + 3
				y = x + 5 * n - 1
				print(x, y)
				# if (sheet2.cell(x, 0).ctype) == 0:
				print(x, y)
				sheet1.write_merge(x, y, 0, 0, year)
				sheet1.write_merge(x, y, 1, 1, month)
				sheet1.write_merge(x, y, 2, 2, day)
				if j > 2:
					time = fields[j]  # 读到的第J个元素加到list（）中
					j = j - 1
					sheet1.write_merge(x, y, 3, 3, time)
					ds1 = xr.open_dataset('d:/D/python/python/CDS%s%s%s' % (year, month, day) + 'h.grib', engine='cfgrib')
					r = ds1['r']
					t = ds1['t']
					ds2 = xr.open_dataset('d:/python/python/CDS%s%s%s' % (year, month, day) + 's.grib', engine='cfgrib')
					ts = ds2['t2m']  # 1000相对湿度
					datar = r.loc['%s-%s-%sT%s' % (year, month, day, time)].loc[1000]  # loc函数查找定位时间，高度层
					a1 = datar.interp(latitude=27.98, longitude=121.02)  # interp函数插值计算
					a2 = float(a1)  # 转为float格式
					a3 = round(a2, 2)  # 取两位小数，round函数非简单四舍五入
					sheet1.write(x, 4, a3)  # 输出到文本必须为字符格式
					b1 = datar.interp(latitude=27.92, longitude=120.86)
					b2 = float(b1)
					b3 = round(b2, 2)
					sheet1.write(x, 5, b3)
					c1 = datar.interp(latitude=27.92, longitude=120.96)
					c2 = float(c1)
					c3 = round(c2, 2)
					sheet1.write(x, 6, c3)
					d1 = datar.interp(latitude=27.82, longitude=120.9)
					d2 = float(d1)
					d3 = round(d2, 2)
					sheet1.write(x, 7, d3)
					sheet1.write(x, 8, '1000hPa相对湿度')
					# else:
					# 	continue
				else:
					pass
				x = x + 1
			else:
				continue
	else:
		pass
	workbook_xlutils.save('D:/d/python/test.xls')


if __name__ == '__main__':
	print2excel()
	pass