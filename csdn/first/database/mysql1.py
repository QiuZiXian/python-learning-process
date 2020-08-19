# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/30  14:52
# @abstract    :

import pymysql
#方式一、连接数据库
db = pymysql.Connect(
    host='121.36.208.96',
    port=3306,
    user='root',
    passwd='root',
    db='rlzy',
    charset='utf8'
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
city = "鞍山4"
phone= "phone:13130158130,"
add = "铁东区矿工路30-s1（长青转盘莱弗仕酒店斜对面）"
company = "爱之潮旗舰店"
sql_f = "INSERT INTO shop(city,phone,address,company) VALUES('{}','{}','{}','{}')".format(city, phone, add, company) # sql插入语句的value需要有单引号
# sql_f = "INSERT INTO shop(city,phone,address,company) VALUES({},{},{},{})".format(city, phone, add, company)
# cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
print(sql_f)
cursor.execute(sql_f)
# 使用后关闭游标和数据库
cursor.close()
# 关闭数据库连接
db.close()