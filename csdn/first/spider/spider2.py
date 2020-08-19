# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/8  14:52
# @abstract    : xlsxwriter的write_row 问题： 写入列表，当列表中的某个值过大时，会造成写入异常，只能使用 for遍历写入 write

import re

import requests

from lxml import etree

import html as ht

import xlsxwriter



def CP_xq(data):

	CPxq=[]

	headers={

	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"

	}

	url1="http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetailViewDesc&prdNo="

	page=0

	with open(data, "r", encoding="utf-8") as f:
		file = f.readlines()

	for line in file:
		if line == "\n":
			continue
		number=re.findall(r'No=(.*?)&tr',line)[0]

		xqurl=url1+str(number)

		xqtext=requests.get(xqurl,headers=headers).text

		xqhtml=etree.HTML(xqtext)

		xq=xqhtml.xpath('//div[@class="ifrm_prdc_detail"]')

		if len(xq)==0:

			xqye=xqhtml.xpath('//div[@class="canvas-content seller-output"]')[0]

			xqpage=etree.tostring(xqye).decode()

			xqhtml=ht.unescape(xqpage)

			zhengque=xqhtml.strip()

			CPxq.append(zhengque)

		else:

			xq=xq[0]

			xqpage=etree.tostring(xq).decode()

			xqhtml=ht.unescape(xqpage)

			zhengque=xqhtml.strip()

			CPxq.append(zhengque)

			# print(zhengque)

		page+=1


		print("添加第"+str(page)+"成功")

		# print(xqurl)
		if page == 25:
			break

	print(len(CPxq))
	for item in CPxq:
		print(item)


	workbook=xlsxwriter.Workbook('11stxp.xlsx')

	worksheet=workbook.add_worksheet('sx')

	headings=['CPxq']

	# worksheet.write_row('A1',headings)

	worksheet.write_column(1, 0,CPxq)
	for i in range(100):
		worksheet.write(i + 1, 0, CPxq[i])

	workbook.close()

	print("属性写入完成")

	print(CPxq[24])

if __name__ == '__main__':

	CP_xq(r'./tmp.txt')