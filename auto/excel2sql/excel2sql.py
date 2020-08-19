# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/4/21  19:03
# @abstract    :	excel数据结构 生成 sql语句


# databaseInfo = 'mysql+pymysql://root:root.123@10.0.75.1:3406/rlzy' # questionnaire
import uuid

from sqlalchemy import create_engine
import pandas as pd


def genUuid5(id):
	return str(uuid.uuid5(uuid.NAMESPACE_DNS, id))[
		   0:32]
databaseInfo = 'mysql+pymysql://root:root@121.36.208.96:3306/rlzy' # questionnaire
engine = create_engine(databaseInfo, encoding="utf-8", echo=True)
tableName = "donate_detail"	# 表名 donate_detail
fileName = "D:/d/python/112.xls"

books = pd.ExcelFile(fileName)
print(books.sheet_names)
# print(books.) # ['企事业单位捐款', '个人汇款']

# for sheetName in books.sheet_names: # , sheet_name='个人汇款'
excel = pd.read_excel(fileName, header=1, index_col=None, sheet_name='个人汇款')  # header=2指定第二行为字段名，index_col=0指定第一列为索引列； 索引从0 ,sheet_name=sheetName
print(excel.shape)
print(type(excel))
print("============================")
print(excel.head(5).values)

tableAllInfo = pd.read_sql_table(tableName, engine)
print(tableAllInfo.head(5))
# print(list(tableAllInfo))
# print(tableAllInfo)
# excel = pd.read_excel(fileName, skiprows=2, index_col=1)
# print(excel.head(5))
# print(excel.iloc[[0, 5]])
print("============================")
print(excel.iloc[2])

headers = list(tableAllInfo)
# dfs = pd.DataFrame(excel, columns=headers)
excel.columns = ["A", "B", "C", "D"]
excel["A"] = ["2020-05-10"] * excel.shape[0]
excel["E"] = [genUuid5(str(i)) for i in  range(1+ 103 +37 + 225, len(excel) + 1+ 103 + 37 + 225)] # + 103  + 37 + 225 + 109
df = excel.reindex(columns=list('EABCD'))
print(df.head(5))
df.columns = headers
print(df.head(5))

# print(excel)
df.to_sql(tableName, engine, if_exists='append', index=False,index_label="id", chunksize=1000) # parse_dates={'Date': {'format': '%Y-%m-%d %H:%M:%S'}

