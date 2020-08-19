# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/22  21:23
# @abstract    :

import re

headers = (
'''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Cookie:_ga=GA1.2.1053266000.1564734163; _gid=GA1.2.979133678.1564734163
Host:fz.maitian.cn
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER
'''
)

headers = (
	'''
_ec_ismobile	true
_ec_browser	EMobile
_ec_browserVersion	7.0.33.20200304
_ec_os	Android
_ec_osVersion	10
ismobile	1
	'''
)

headers = (
    '''
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh,en-US;q=0.9,en;q=0.8,ca;q=0.7,zh-CN;q=0.6
Cache-Control: no-cache
Cookie: yfx_c_g_u_id_10000042=_ck20080410433418134739970535937; VISITED_MENU=%5B%228466%22%5D; JSESSIONID=CC60E4FCAE159CF6F64846720CF3AEA3; yfx_f_l_v_t_10000042=f_t_1596509014813__r_t_1596509014813__v_t_1596515280240__r_c_0
Host: query.sse.com.cn
Pragma: no-cache
Proxy-Connection: keep-alive
Referer: http://www.sse.com.cn/market/stockdata/overview/day/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
    '''
    )

def headToDict(headers, sep=":"):
	headers_dict = {}
	headers_list = headers.split("\n")
	for item in headers_list:
		# print(item)
		if item:
			try:
				headers_dict[item.split(sep, 1)[0].strip()] = item.split(sep, 1)[-1].strip()
			except:
				pass
	if headers_dict:
		print('{')
		for item in headers_dict.items():
			print(str(item).lstrip('(').rstrip(')').replace(',', ':'), ',')
		print('}')
	return headers_dict

if __name__ == '__main__':
	print(headToDict(headers))
