# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/23  14:04
# @abstract    :

import scrapy

class MySpider():

	def startRequest(self):
		request_with_cookies = scrapy.Request(url="http://www.example.com",
									   cookies={'currency': 'USD', 'country': 'UY'})
		return request_with_cookies

	def parse(self, response):
		request = scrapy.Request('http://www.example.com/index.html',
								 callback=self.parse_page2,
								 cb_kwargs=dict(main_url=response.url))
		request.cb_kwargs['foo'] = 'bar'  # add more arguments for the callback
		yield request

	def parse_page2(self, response, main_url, foo):
		yield dict(
			main_url=main_url,
			other_url=response.url,
			foo=foo,
		)

if __name__ == '__main__':
	demo = MySpider()
	demo.parse()