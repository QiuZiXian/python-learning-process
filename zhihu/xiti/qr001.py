# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/22  20:36
# @abstract    :	优惠券激活码生成、 保存到mysql、 保存到redis

'''

1、 激活码：
	大小写、数字
	区分大小写
	16位

2、 python 连接数据库
3、 python 连接redis
3、 python的随机函数random
'''
import random
import pymysql
# alnum = [chr(num) for num in range(48,58)] + [chr(num) for num in range(65, 91)] + [chr(num) for num in range(97, 123)]
# # alnum = range(48,58) + range(65, 91) + range(97, 123)
#
# print("".join(alnum))

alnum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

sample = random.sample(alnum, 16)
print(sample)

def getSample(length):
	"""
	随机生成length长度的列表
	来源：大小写、数字
	:param length: 选取长度
	:return: sample为list
	"""
	alnum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	sample = random.sample(alnum, length)

	return sample


def connect():
	db = pymysql.Connect(
		host='121.36.208.96',
		port=3306,
		user='root',
		passwd='root',
		db='rlzy',
		charset='utf8'
	)
	return db
db = connect()
cursor = db.cursor()


def creatTableSql(tableName,fields, auto=True):
	"""
		简单 建表 sql语句生成
	:param tableName: 创建表的 表名
	:param fields: 表的 字段列表	--> 待扩展至 指定字段类型
	:param auto: 默认自动创建主键id
	:return:
	"""
	ctSql = "CREATE TABLE IF NOT EXISTS `{}` (\n".format(tableName)
	autoKey = "`id` INT NOT NULL AUTO_INCREMENT,\n"
	if auto:
		ctSql = ctSql + autoKey
	for index in range(len(fields) - 2) :
		ctSql = ctSql + "`{}` VARCHAR(25),\n".format(fields[index])
	if auto:
		ctSql = ctSql + "PRIMARY KEY (`id`),\n"
	ctSql = ctSql + "`{}` VARCHAR(25)\n".format(list(fields)[-1])
	ctSql = ctSql + ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"

	return ctSql
# 建表
# fields = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]
# tableName = "code"

def excuteSql(cursor, sqls):
	cursor.execute(sqls)


for i in range(200):
	sample = getSample(16)
	sql_one = "INSERT INTO qrcode(qrcode) VALUES('{}')".format("".join(sample))
	excuteSql(cursor, sql_one)
cursor.close()
db.close()


# excuteSql(creatTableSql(tableName, fields))
print("ok!")
