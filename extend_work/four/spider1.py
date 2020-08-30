# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/26  11:27
# @abstract    :


# import requests
# from lxml import etree
# from bs4 import BeautifulSoup
#
#
# import requests
# from lxml import etree
#
# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
#     'Host': 'book.douban.com'
# }
#
# # html = requests.get(url='https://book.douban.com/latest', headers=headers)
# # html = etree.HTML(html.text)
#
# # print(html.xpath('//li/div[@class="detail-frame"]/h2/a/text()'))
# root_url = 'https://book.douban.com/'
# r = requests.get(root_url, headers=headers)
# # print(r)
# # soup = BeautifulSoup(r.text, 'lxml')
# # print(soup)
# dom = etree.HTML(r.text)
# print(dom.xpath('//*[@id="content"]/div/div[1]/div[6]/div[2]/ul/li[2]/div[2]/div[1]/a/text()'))


import  numpy as np

# x = np.array([[[1, 4, 7, 4],
#
# [2, 5, 8, 5],
#
# [3, 6, 9, 6]],
#
# [[10, 40, 70, 7],
#   [20, 50, 80, 8],
#
# [30, 60, 90, 9]],
#
# [[100, 400, 700, 10],
#
# [200, 500, 800, 11],
#
# [300, 600, 900, 11]]])
# print(x)
# print('This tensor is of rank %d' %(x.ndim))
# print('This tensor is of shape ' ,x.shape)


tonsor_4 = np.random.normal(0, 1, (3, 3, 4, 4))
print(tonsor_4)
print(tonsor_4.ndim)

