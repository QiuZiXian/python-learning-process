# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/22  19:46
# @abstract    :	模拟post、 get等请求



# python3.5
import requests
from urllib import parse
url = "你的url"
data= {
   "cmd":"mget",
   "args":["offline_lp_all", "offline_qsb_all"]
}
data = parse.urlencode(data)
response = requests.post(url,data=data)
print(response)