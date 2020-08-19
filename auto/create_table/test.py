# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/3/30  9:16
# @abstract    :

import re

filePath = "D:/d/python/python/数据库文档.md"

permitNull = {"YES": "NULL DEFAULT NULL",
			  "NO": "NOT NULL"}


def handleField(field):
	if field:
		return field.strip("\n").strip(" ").strip("\n")

with open(filePath, "r", encoding="utf-8") as f:
	data = f.readlines()
	print(data)
	print("======================")
	# for item in data:
	# 	print(item)
tables_dict = {}
data = list(filter(None, data))
data = [item for item in data if not item.isspace()]
pattern_tableName = r'[（|(](.+?)[)|）]'
for index, item in enumerate(data):
	if item.startswith("###"):
		tableName = index
		tmp = index
		try:
			tableName = re.search(pattern_tableName, item).group(1)
		except:
			print("表名匹配失败，请确认格式======={}========".format(item))
	else:
		if index == tmp + 1 or index == tmp + 2:
			continue
		pattern_fieldInfo = r'(.* )\| (.*) \| \| (YES|NO) \| (.*)\n$'
		fieldInfo = re.search(pattern_fieldInfo, item, re.L)
		if fieldInfo:
			if tableName in tables_dict:
				tables_dict[tableName].append(fieldInfo.groups())
			else:
				tables_dict[tableName] = [fieldInfo.groups()]
		else:
			print("{0}该表的========={1}=======".format(tableName, item))
print(len(tables_dict))
for k, v in tables_dict.items():
	print(k)
	for item in v:
		print(item)
# pattern_one = r'------- |--------- |--------|  ---------| -----|(.+?)\n\n'
# ones = re.findall(pattern_one, re.sub(r'\n{2,}', "\n\n", data), re.S)
# ones = data.split("\n\n")
# ones = list(filter(None, ones))
# print(len(ones))
# for index, one in enumerate(ones):
# 	print(str(index) + "==========================>")
# 	print(one)
	# one = one.group(1)
	# '### 1、 （staff_info_mirror）福建省电子信息集团本部人员名册'
	# pattern_tableName = r'\（(.+)\）'
	# tableName = None
	# try:
	# 	tableName = re.search(pattern_tableName, one).group(1)
	# 	print(tableName)
	# except:
	# 	pass
	# pattern_fieldInfo = r'(.* )\| (.*) \| \| (YES|NO) \| (.*)\S$'
	# fieldInfo = re.findall(pattern_fieldInfo, one)
	# for item in fieldInfo:
	# 	print(item)

	# table_sql_pre = '''
	# 	DROP TABLE IF EXISTS `{0}`;
	# CREATE TABLE `{0}`  (
	# '''.format(handleField(tableName))
	#
	# for item in fieldInfo:
	# 	table_sql_pre = table_sql_pre + "`{0}` {1} {2} COMMENT '{3}',\n".format(
	# 		handleField(item[0]), handleField(item[1]), permitNull[item[2]], handleField(item[3]))
	#
	# table_sqls = table_sql_pre.rstrip(",\n") + "\n) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;\n" + "SET FOREIGN_KEY_CHECKS = 1;"
	# print(ones.index(one))
	# print(table_sqls)
	# with open("createTableBat.sql", "a", encoding="utf-8") as f:
	# 	f.write(table_sqls)


