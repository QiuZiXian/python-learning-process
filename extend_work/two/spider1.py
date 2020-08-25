# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/21  16:27
# @abstract    :

import requests
import json
response = requests.get("http://www.qqssss.com/files/8位QQ【1号单】-不带4『45一个,带1个月超会』共20175个.txt")


print(json.loads(response.text))