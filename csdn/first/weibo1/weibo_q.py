# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/1  12:44
# @abstract    :	提问者代码


import requests
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import re

def get_url(pageNum):
	url = 'https://book.douban.com/subject/34995610/comments/hot?p={pageNum}'.format(pageNum=pageNum)

	return url

# import requests
headers = {

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML: like Gecko) Chrome/83.0.4103.116 Safari/537.36' ,
}
# response = requests.get("https://book.douban.com/subject/34995610/comments/hot?p=1",headers=headers)
# print(response.text)
tmp = []

# for pageNum in range(1, 2):
# 	response = requests.get(get_url(pageNum), headers=headers)
# 	# response.encoding="utf-8"
# 	response.encoding ="utf-8"
# 	# print(response.content.decode("utf-8"))
# 	# print(response.content)
# 	soup = BeautifulSoup(response.content, "lxml")
# 	all = soup.find_all("span", {"class":"short"})
# 	print(all)
# 	for item in all:
# 		tmp.append(item.text)
# for item in tmp:
# 	print(item)
# with open("D:/d/python/python/douban.txt", "w", encoding="utf-8") as f:
# 	f.write(response.text)


print("ok")

def get_url(n):
    url = 'https://book.douban.com/subject/34995610/comments/hot?p='
    url = url+str(n)
    return url
reviewbox = list()
allstars = list()
count = 0
for page in range(1,3):
    r=requests.get(get_url(page),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
    soup = BeautifulSoup(r.content,'lxml')
    review = soup.find_all("span",{"class":"short"})
    stars_pattern = re.compile(r'<span class="user-stars allstar(.*?) rating"')
    stars = stars_pattern.findall(r.text)
    for istar in stars:
        if count < 50 :
            istar = int(istar)
            allstars.append(istar)
            count = count + 1
    for i in review:
        reviewbox.append(i.text)
#print(reviewbox)
print(allstars)
print(len(allstars))
for i1 in reviewbox:
    with open (r'reviews.txt','a',encoding='utf-8') as  file:
        file.write(i1)
with open("D:/d/python/python/douban.txt", "w", encoding="utf-8") as f:
	f.writelines(reviewbox)

with open("D:/d/python/python/douban.txt",'r',encoding='utf-8') as file:
    reviews = file.read()
reviews = reviews.replace('jc','警察')
# pattern = re.compile(r'([\u4e00-\u9fa5,，。·,0-9]+|\n)')
pattern = re.compile(r'([^\u4e00-\u9fa5,，。·,0-9]+|\n)')
data_reviews = re.sub(pattern, "", reviews)
# deal_reviews = re.findall(pattern,reviews)
# newreviews = ''
# for item in deal_reviews:
#     newreviews = newreviews + item
print('所有短评:\n',data_reviews)
# avestars = sum(allstars)/50
# print('前50条短评综合平均得分：',avestars)
# result = jieba.lcut(open('reviews.txt',encoding='utf-8').read())
# imageobj = Image.open('background.jpg')
# cloud_mask = np.array(imageobj)
# #绘制词云
# wc = wordcloud.WordCloud(
#     mask=cloud_mask,
#     background_color='black',
#     font_path='simsun.ttc',  # 处理中文数据时使用的字体形式
#     min_font_size=5,  # 图片中最小字体大小；
#     max_font_size=50,    # 图片中最大字体大小；
#     width=500,  # 指定生成图片的宽度
# )
# wc.generate(','.join(result))
# wc.to_file('八百万种死法词云.png')
# 这个是我现在得代码