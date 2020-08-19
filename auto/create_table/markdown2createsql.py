# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/3/30  18:39
# @abstract    :
import re, os

filePath = "D:/d/python/python/数据库文档.md"
sqlFile = "createTableBat1.sql"


permitNull = {"YES": "NULL DEFAULT NULL",
			  "NO": "NOT NULL"}
def handleField(field):
	if field:
		return field.strip("\n").strip(" ").strip("\n")


def readMarkdown():
	with open(filePath, "r", encoding="utf-8") as f:
		data = f.readlines()
	return data


def handleSourceData(data):
	data = list(filter(None, data))
	data = [item for item in data if not item.isspace()]
	return data


def parseData(data): # 解析数据 {tableName: [各个字段数据]}
	tables_dict = {}
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

	return tables_dict


def genSqls(tableName, fieldInfo):
	table_sql_pre = '''
		DROP TABLE IF EXISTS `{0}`;
		 CREATE TABLE `{0}`  (
		 '''.format(handleField(tableName))

	for item in fieldInfo:
		table_sql_pre = table_sql_pre + "`{0}` {1} {2} COMMENT '{3}',\n".format(
			handleField(item[0]), handleField(item[1]), permitNull[item[2]], handleField(item[3]))

	table_sqls = table_sql_pre.rstrip(
		",\n") + "\n) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;\n" + "SET FOREIGN_KEY_CHECKS = 1;"

	# print(table_sqls)
	return table_sqls


def delOldSqlsFile():
	if os.path.isfile(sqlFile):
		os.remove(sqlFile)


def genSqlFile(table_sqls):
	with open(sqlFile, "a", encoding="utf-8") as f:
		f.write(table_sqls)


def isQurifyFile():
	pass
	return True

def execSql():
	pass

def main():
	data = readMarkdown()
	if isQurifyFile():
		delOldSqlsFile()
		table_dict = parseData(handleSourceData(data))
		for tableName, fieldInfo in table_dict.items():
			sqls = genSqls(tableName, fieldInfo)
			genSqlFile(sqls)



if __name__ == '__main__':
	main()
	execSql() # 生成的sql语句中，可能由于markdown中的异常格式而无法对某些字段进行解析
