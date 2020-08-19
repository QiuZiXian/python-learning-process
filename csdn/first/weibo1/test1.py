# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/1  13:05
# @abstract    :

from akufire.headToDict import headToDict

headerStr = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh,en-US;q=0.9,en;q=0.8,ca;q=0.7,zh-CN;q=0.6
Cache-Control: no-cache
Connection: keep-alive
Cookie: bid=Pq8TsxJmLd8; ap_v=0,6.0; __utma=30149280.1011887727.1593578977.1593578977.1593578977.1; __utmc=30149280; __utmz=30149280.1593578977.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_douban=1; __utmb=30149280.1.10.1593578977; __utma=81379588.603654688.1593578977.1593578977.1593578977.1; __utmc=81379588; __utmz=81379588.1593578977.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=81379588.1.10.1593578977; _pk_id.100001.3ac3=5b1b0675659b7b7b.1593578977.1.1593578977.1593578977.; _pk_ses.100001.3ac3=*
Host: book.douban.com
Pragma: no-cache
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
'''
headerStr = '''
Host	fy.nebedu.cn:8093
Content-Length	1589
Origin	http://fy.nebedu.cn:8093
User-Agent	Mozilla/5.0 (Linux; Android 10; V1824A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2469 MMWEBSDK/200502 Mobile Safari/537.36 MMWEBID/3858 MicroMessenger/7.0.15.1680(0x27000F3F) Process/tools WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64
Content-Type	application/json;charset=UTF-8
Accept	*/*
X-Requested-With	com.tencent.mm
Referer	http://fy.nebedu.cn:8093/
Accept-Encoding gzip, deflate
Accept-Language zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cookie acto=b16a2703ab5b4f419f21ac9955b61548
Connection keep-alive
'''
print(headToDict(headerStr))


s = " abc "
print(s)
print(s.strip())

import sys


print(sys.getdefaultencoding())#查看系统默认字符编码格式



li = [1, 22]

print(lambda x:x+1)