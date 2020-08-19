# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/28  13:13
# @abstract    :

list1 = [
    {"Name": "张三", "Sex": "男", "PhoneNumber": "13711111111"},
    {"Name": "李四", "Sex": "女", "PhoneNumber": "13811111111"},
    {"Name": "王五", "Sex": "女", "PhoneNumber": "13912345678"}
]
searchName=input("请输入您要查找的姓名？")
for item in list1:
    if item["Name"] == searchName:
        print("您要查找的{0}的电话是{1}".format(searchName,item["PhoneNumber"]))
        break
searchName = input("请输入您要修改性别的姓名？")
gender=input("请输入您要设置的性别？")
for item in list1:
    if item["Name"] == searchName:
        item["Sex"] = gender
        print("已经把{0}的性别修改为{1}".format(searchName,item["Sex"]))
        break
phone=input("请输入您要查找的电话号码？")
for item in list1:
    if item["PhoneNumber"] == phone:
        print("你要查找的{0}的名字为为{1}".format(phone,item["Name"]))
        break
list1.append(
    {"Name": "王五2", "Sex": "女", "PhoneNumber": "13287651234"}
)
print("新增了一条记录，现在的列表内容是{0}".format(list1))