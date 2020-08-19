# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/9  19:43
# @abstract    :

from dbfread import DBF
import dbf
from struct import *

# # # table = DBF('1.DBF',encoding='gbk', load=True)
# table = DBF('0.DBF', char_decode_errors='ignore', raw=True)
# # table.load()
# # fields = table.field_names
# #
# for item in table.load():
# 	print(item)
#

table = dbf.Table("0.DBF", codepage="cp936")
table.open()
print(table.field_names)
for item in table:
	print(item)
# # table.
# for item in table:
# 	try:
# 		print(item.decode("gbk"))
# 	except:
# 		continue

# with dbf.Table("0.DBF") as table:
# 	dbf.export(table, "test.csv", encoding="utf-8")
# print(table)
# print(len(table))
#

# import dbf
#
# codepage_list = ['936', '437', ...]
#
# for codepage in codepage_list:
#
#     table = dbf.Table('0.dbf', codepage='cp{}'.format(codepage))
#     table.open(dbf.READ_WRITE)
#     try:
#         for row in table:
#             print(row)
#         table.close()
#     except UnicodeDecodeError:
#         print('wrong codepage', codepage)
#         table.close()
#         continue


