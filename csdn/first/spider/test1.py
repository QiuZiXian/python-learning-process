# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/8  15:07
# @abstract    :


# with open(r"./tmp.txt", "r", encoding="utf-8") as f:
# 	file = f.readlines()
# for item in file:
# 	if item != "\n":
# 		print(item)

import xlsxwriter
workbook=xlsxwriter.Workbook('11stxp.xlsx')

worksheet=workbook.add_worksheet('sx')

# headings=['CPxq']

# worksheet.write_row('A1',headings)
data = ["123ajogjoba bj qavajlaj"*10000]*25

print(len(data))

worksheet.write_column(1, 0,data)
workbook.close()

print("属性写入完成")



# data = ('Foo', 'Bar', 'Baz')
# # write_column 方法写入
# worksheet.write_column('A1', data)
#
# # 上述write_column 方法写入与下面 等效
# worksheet.write('A1', data[0])
# worksheet.write('A2', data[1])
# worksheet.write('A3', data[2])