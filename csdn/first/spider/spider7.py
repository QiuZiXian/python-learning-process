# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/31  13:28
# @abstract    :

# 如果要全部的数据

import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Mobile Safari/537.36'
}
url = 'https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=1&stage=publish&callback=jsonp'
res = requests.get(url=url,headers=headers)
obj = json.loads(res.text[6:-2])
usa = list(filter(lambda v: v['name']=='美国' , obj['data']))[0]
updateDate = usa['trend']['updateDate']
data = usa['trend']['list']
for i,u in enumerate(updateDate):
    print("日期:",u,
        data[3]['name']+':',data[3]['data'][i],
        data[0]['name']+':',data[0]['data'][i],
        data[1]['name']+':',data[1]['data'][i],
        data[2]['name']+':',data[2]['data'][i]
    )