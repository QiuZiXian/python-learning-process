# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/1  19:08
# @abstract    :


import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re


# 获取每页 的url，即翻页
def get_url(pageNum):
	url = 'https://book.douban.com/subject/34995610/comments/hot?p={pageNum}'.format(pageNum=pageNum)
	return url


headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML: like Gecko) Chrome/83.0.4103.116 Safari/537.36' ,
}

def getRawReview(): # 返回值 为单层列表
	rawReview = [] # 暂存原生数据
	for pageNum in range(1, 26):
		response = requests.get(get_url(pageNum), headers=headers)
		response.encoding="utf-8" # 返回值编码，通常为utf-8，可根据实际调整
		soup = BeautifulSoup(response.text, 'lxml')
		reviews = soup.find_all("span", {"class": "short"})
		rawReview.extend([review.text for review in reviews])
	# print(rawReview)
	return rawReview


# 本地txt写入及读取；txt会有 chunk问题，量少则不用担心
def saveToTxt(filename, content): # content为列表时写入本地 的函数
	with open(r'reviews.txt', 'w', encoding='utf-8') as  file:
		file.writelines(content)
def loadFromTxt(filename): # 一次性读取
	with open(r'reviews.txt', 'r', encoding='utf-8') as  file:
		content = file.read()
	return content

def handleRawData(rawData): # 爬取的原始数据处理函数, rawData为str
	# 一些 敏感词 还原
	tmp = rawData.replace("jc", "警察")

	# 去掉不需要的字符
	pattern_need = re.compile(r'([^\u4e00-\u9fa5,，。·,0-9]+|\n)')
	result = re.sub(pattern_need, "", tmp)


	# 一些 特殊情况处理
	pattern_time = re.compile(r'[-\d]{5,}')
	result = re.sub(pattern_time, "", result) # 去掉时间
	return result
filepath = r'reviews.txt' # 文件名，文件存取为当前路径
def spider():
	# filepath = r'reviews.txt' # 文件名，文件存取为当前路径
	rawData = getRawReview()  # 爬取原始数据
	saveToTxt(filepath, rawData)


# spider() # 一次性爬取，后续制作load本地数据处理即可
rawData = loadFromTxt(filepath) # 加载本地数据
result = handleRawData(rawData) # 数据处理
print(result)