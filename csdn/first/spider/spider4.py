# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/23  12:24
# @abstract    :
import scrapy

import xlrd

from YelpSpider.items import YelpspiderItem



class YelpSpiderSpider(scrapy.Spider):

	name = 'yelp_spider'

	allowed_domains = ['www.yelp.com']

	# start_urls = ['http://www/']

	def start_requests(self):

		base_url = 'https://www.yelp.com/search?find_desc='

		address_file = xlrd.open_workbook(r'D:\工作\YelpSpider\YelpSpider\data\h_z.xlsx')

		k_file = xlrd.open_workbook(r'D:\工作\YelpSpider\YelpSpider\data\key_word.xlsx')

		add_table = address_file.sheets()[0]

		k_table = k_file.sheets()[0]

		k_nrows = add_table.nrows

		add_nrows = add_table.nrows

		for k in range(k_nrows):

			ke = k_table.row_values(k)[0]

		for add in range(add_nrows):

			city = add_table.row_values(add)[0]

			province = add_table.row_values(add)[2]

			province_s = add_table.row_values(add)[1]

			add_url = city+","+"+"+province_s

			ke_url = ke.replace(' ','+')

			fin_url = base_url+ke_url+'&find_loc='+add_url+'&start=00'

			sim_url = base_url+ke_url+'&find_loc='+add_url+'&start='

			meta = {"province":province,'sim_url':sim_url}

		yield scrapy.Request(url=fin_url, callback=self.parse,meta=meta)







	def parse(self, response):

		print("我进来了")

		try:

			sim_url = response.meta["sim_url"]

			ye_se = response.xpath('//*[@id="wrap"]/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/span/text()').extract_first()

			ye = int(ye_se.replace('1 of ',''))

			for i in range(ye):

				next_url = sim_url+str(i*10)

				province = response.meta['province']

				meta = {'province': province}

				print('我出去了')

			yield scrapy.Request(url=next_url, callback=self.parse_detail,meta=meta,dont_filter=True)

		except:

			print('我没有值了')

			item = YelpspiderItem()

			item['keyword'] = None

			item['city'] = None

			item['phone_number'] = None

			item['address'] = None

			item['web'] = None

			item['provinc'] = None

			yield item

	def parse_detail(self,response):

		print(2222222222222)

		print("shshhsshshsh"+response.url)

		print(response.meta['province'])

		detail_url_list = response.xpath('//*[@id="wrap"]/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li/div/div/div/div/div/div/div/div/div/div/div/a/@href').extract()

		for url in detail_url_list:

		detail_url = 'https://www.yelp.com'+url

		province = response.meta['province']

		meta={'province':province}


if __name__ == '__main__':
