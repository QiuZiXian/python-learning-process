# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/11  9:49
# @abstract    :


import requests

import random

from lxml import etree
import pandas as pd

useragentlist=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',

'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',

'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',

'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',

'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',

'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',

'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',

'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',

'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',

'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',

'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',

'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',

'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',

'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',

'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',

'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',

'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)']

useragent=random.choice(useragentlist)

headers={'User-Agent':useragent}

data = []
for i in range(1,3):

	url='https://www.chinahr.com/channel/bj/pn'+str(i)+'/'

	print('开始请求第',i,'p')

	# r'https://www.chinahr.com/detail/bj/chaoshishangye/43148623750156x.shtml?psid=166578670209334923158158688&from=channel'

	# // *[ @ id = "assortment_right"] / div[2] / ul / li[1] / div[3] / div[2] / a

	# // *[ @ id = "assortment_right"] / div[2] / ul / li[2] / div[3] / div[2] / a

	response=requests.get(url,headers=headers).text

	html=etree.HTML(response)

	positions=html.xpath('// *[ @ id = "assortment_right"] / div[2] / ul / li / div[3] / div[2] / a/@href')
	for position in positions:

		response=requests.get(position,headers=headers).text

		html=etree.HTML(response)

		companyName=html.xpath('/html/body/div[4]/div/div[2]/div/span[1]/text()') # /html/body/div[4]/div/div[2]/div/span[1]


		address=html.xpath('/html/body/div[4]/div/div[1]/div[3]/span/text()')
		try:
			companyName=companyName[0]

			address=address[0]
		except:
			companyName = "false"
			address = "false"
		item = [companyName, address]
		data.append(item)

df = pd.DataFrame(data)
df.to_excel("data.xlsx")