# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/17  10:29
# @abstract    :

import json

data = {"b":{"1":"2", "3":"4"}}

with open("test.json", "r", encoding="utf-8") as f:
	s = json.load(f)
	s.update(data)
with open("test.json", "w", encoding="utf-8") as f:
	json.dump(s,f)