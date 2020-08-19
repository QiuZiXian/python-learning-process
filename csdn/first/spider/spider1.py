# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/8  14:39
# @abstract    :



import re
import requests
from lxml import etree
import html as ht
import xlsxwriter

def CP_xq(data):
	CPxq = []
	headers = {

	}
	url1 = "http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetailViewDesc&prdNo="
	page = 0
	with open(data, "r", encoding="utf-8") as f:
		file = f.read()
	for line in file:
		number = re.findall(r'No=(.*?)&tr', line)[0]
		xqurl = url1 + str(number)
		xqtext = requests.get(xqurl, headers=headers).text
		xqhtml = etree.HTML(xqtext)
		xq = xqhtml.xpath('//div[@class="ifrm_prdc_detail"]')
		if len(xq) == 0:
			xqye = xqhtml.xpath('//div[@class="canvas-content seller-output"')[0]
			xqpage = etree.tostring(xqye).decode()
			xqhtml = ht.unescape(xqpage)
			zhengque = xqhtml.strip()
			CP_xq(zhengque)
		else:
			xq = xq[0]

