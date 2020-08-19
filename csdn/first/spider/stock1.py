# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:47:55 2020

@author: 87875
"""

import requests,json

headers = {
'Accept': '*/*' ,
'Accept-Encoding': 'gzip: deflate' ,
'Accept-Language': 'zh:en-US;q=0.9:en;q=0.8:ca;q=0.7:zh-CN;q=0.6' ,
'Cache-Control': 'no-cache' ,
'Cookie': 'yfx_c_g_u_id_10000042=_ck20080410433418134739970535937; VISITED_MENU=%5B%228466%22%5D; JSESSIONID=CC60E4FCAE159CF6F64846720CF3AEA3; yfx_f_l_v_t_10000042=f_t_1596509014813__r_t_1596509014813__v_t_1596515280240__r_c_0' ,
'Host': 'query.sse.com.cn' ,
'Pragma': 'no-cache' ,
'Proxy-Connection': 'keep-alive' ,
'Referer': 'http://www.sse.com.cn/market/stockdata/overview/day/' ,
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML: like Gecko) Chrome/84.0.4147.105 Safari/537.36' 
}
url = "http://query.sse.com.cn/commonQuery.do?jsonCallBack=jsonpCallback88354&searchDate=&sqlId=COMMON_SSE_SJ_GPSJ_CJGK_DAYCJGK_C&stockType=90&_=1596509137699"
response = requests.get(url,headers=headers)

print(response.text[19:-1])

import json
result = json.loads(response.text[19:-1])
print(result["result"])