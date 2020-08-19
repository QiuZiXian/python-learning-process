# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/28  16:38
# @abstract    :

import requests,json

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',

        }
url = "https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=s&da_src=shareurl&wd=%E6%88%90%E4%BA%BA%E7%94%A8%E5%93%81%E5%95%86%E5%BA%97&c=340&src=0&pn=0&sug=0&l=13&b=(12643795,2568725;12704019,2597781)&from=webmap&biz_forward=%7B%22scaler%22:1,%22styles%22:%22pl%22%7D&device_ratio=1&auth=D48xWgcNIJHPc4xzaJM7ObgJ2QQEUxc9uxHTHTzzTVVtComRB199A1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuVtPYIuVtcvY1SGpuNtZComRdXmB1F234Q6W89AcEWe1GD8zv7u%40ZPuVteuVtegvcguxHTHTzzTVVteh33uVtrZZWuV&tn=B_NORMAL_MAP&nn=0&u_loc=12670907,2580253&ie=utf-8&t=1595922899525"
res = requests.get(url,headers=headers).text.encode('latin-1').decode('unicode_escape')
i = json.dumps(res)

res = requests.get(url,headers=headers).text.encode('latin-1').decode('unicode_escape')
match = re.findall('("content":"(.*?)")',res,re.M|re.I)
print(match)