# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/22  19:15
# @abstract    :

from selenium import webdriver as wb

from selenium.webdriver.common.action_chains import ActionChains

import time,csv,codecs,queue,requests,json,math,re

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed

from selenium.common.exceptions import StaleElementReferenceException,UnexpectedAlertPresentException

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import By

from selenium.webdriver.chrome.options import Options

from queue import Queue

import threading





class Yaosb(object):



	def __init__(self):

		options = Options()

		options.headless = True

		options.add_argument('--disable-gpu')

		self.driver = wb.Chrome()

		self.executor = ThreadPoolExecutor(max_workers=4)

		self.driver1 = wb.Chrome()

		self.driver2 = wb.Chrome()

		self.driver3 = wb.Chrome()

		self.driver4 = wb.Chrome()



	def login(self): # 登录网站

		self.driver.implicitly_wait(10)

		self.driver.get('https://dian.ysbang.cn/#/login')

		self.driver.find_element_by_id('userAccount').clear()

		self.driver.find_element_by_id('userAccount').send_keys('18075161006')

		self.driver.find_element_by_id('password').clear()

		self.driver.find_element_by_id('password').send_keys('18075161006')

		pic_url = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#captchaImg'))).get_attribute('src')

		print(pic_url)

		resp = requests.get(pic_url).content

		with open(r'C:\Users\25808\Desktop\python_work\验证码.png','wb') as f:

		f.write(resp)

		iden_code = input('请输入验证码：')

		self.driver.find_element_by_id('captcha').send_keys(iden_code)

		self.driver.find_element_by_id('loginBtn').click()



	def get_target_page(self): # 进入目标页面

		self.login()

		while True:

			try:

				self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_css_selector('.goto-index.router-link-active'))

				element1 = self.driver.execute_script("return document.querySelector('.parent-list-box div')")

				ActionChains(self.driver).move_to_element(element1).perform()

				element2 = self.driver.execute_script("return document.querySelector('.parent-list-box li.parent-list-item')")

				self.driver.execute_script("arguments[0].click();",element2) # 进入分类界面

				element3 = self.driver.execute_script("return document.querySelector('div.class-select.item_0 a')")

				ActionChains(self.driver).move_to_element(element3).perform()

				element4 = self.driver.execute_script("return document.querySelector('div.class-select.item_0 div.classitem a')")

				self.driver.execute_script("arguments[0].click();",element4) # 进入所有商家界面

				break

			except Exception as e:

				print(f'展开商家界面失败，错误信息：{e}，休息3秒后.....重新操作！')

			time.sleep(3)



	def main(self, driver, cookies): # 统计供应商数量

		i = 0 if driver == self.driver1 else 1 if driver == self.driver2 else 2 if driver == self.driver3 else 3 if driver == self.driver4 else ''

		for s in (p+i for p in range(900) if p % 4 == 0 and p > 104):

			print(f'进入主程序，操作第{s+1}个商家！')

			driver.get('https://dian.ysbang.cn/index.html#/indexContent')

		for cookie in cookies:

			driver.add_cookie(cookie)

			driver.get('https://dian.ysbang.cn/index.html#/indexContent')

		while True:

			try:

				element5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#wrapper > div.filters > div:nth-child(1) > div.filter-content > div.list > div.list-btn > a.more-btn')))

				driver.execute_script("arguments[0].click();", element5)

				element8 = driver.find_elements_by_css_selector('.condition div.item')[3]

				driver.execute_script("arguments[0].click();", element8) # 选中有货

				time.sleep(2)

				sup_index = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.loading ul.autoHeight a')))

				sup_nums = len(sup_index)

				print('共：' + str(sup_nums) + '个商家')

				if sup_nums > 800 and element8.text == '有货':

				break

			except Exception as e:

				print(f'所有商家信息获取失败，错误信息:{e},现休息3秒后...重新操作！')

				time.sleep(3)

				goods_nums = 0

			for supply in (supply for n, supply in enumerate(sup_index) if n == s):

				supply_name = supply.text

				print(supply_name)

		while True:

			try:

			driver.execute_script("arguments[0].click();", supply)

			time.sleep(5)

			page_nums = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-amount'))).text

			html_goods_nums = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.right'))).text

			html_goods_nums = re.findall(r'共(\d+)', html_goods_nums)[0]

			if math.ceil(int(html_goods_nums) / 60) == int(page_nums):

			print(f'{supply_name}选择成功')

			break

			except Exception as e:

			print(f'商家选择失败，或页面数获取失败，错误信息:{e},现休息5秒后...重新操作！')

			time.sleep(5)

			if int(page_nums) > 333:

			print(f'{supply_name}的商品页数大于330页')

			element6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.class-select')))

			ActionChains(driver).move_to_element(element6).perform()

			sorts = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.class-select div.items a')))

			driver.execute_script("arguments[0].click();", sorts[0])

			print(f'{supply_name}共{len(sorts)}类！')

			for sort in range(len(sorts)):

			while True:

			try:

			element9 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.class-select.item_0')))

			ActionChains(driver).move_to_element(element9).perform()

			sorts = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.class-select.item_0 div.items a')))

			driver.execute_script("arguments[0].click();", sorts[sort])

			sorts_nums = len(sorts)

			print(f'获取药品所有分类数量：{sorts_nums}')

			sort_page_nums = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-amount'))).text

			print(f'获取{sorts[sort].text}类，共{sort_page_nums}页，网上共{math.ceil(int(html_goods_nums) / 60)}页！')

			page_nums = sort_page_nums

			if sorts_nums <= 10 and int(page_nums) < math.ceil(int(html_goods_nums) / 60):

			print(f'{supply_name}数量超过330个，操作分类成功')

			print(driver,page_nums,supply_name,html_goods_nums,goods_nums,s)

			self.loads_info(driver, page_nums, supply_name, html_goods_nums, goods_nums, s)

			print(f'{supply_name}大于330页，下商品去！')

			break

			except Exception as e:

			print(f'{supply_name}的页数超过330页，现获取药品分类失败，错误信息：{e}，等待3秒钟....再次操作！')

			time.sleep(3)

			else:

			print(f'{supply_name}的商品页数少于330页')

			print(driver, page_nums, supply_name, html_goods_nums, goods_nums, s)

			self.loads_info(driver, page_nums, supply_name, html_goods_nums, goods_nums, s)

			print(f'{supply_name}少于330页，下商品去！')



	def loads_info(self, driver, page_nums, supply_name, html_goods_nums, goods_nums, s):

		print(f'{supply_name}进入下载商品代码成功，共{page_nums}页')

		for page_num in range(int(page_nums)):

		while True:

		try:

		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-go'))).clear()

		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-go'))).send_keys(int(page_num)+1)

		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-submit'))).click()

		goods_infos = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.drug-drugInfo')))

		page_goods_nums = len(goods_infos)

		print(f'{supply_name}第{page_num}页，共{page_goods_nums}个商品')

		if page_num != int(page_nums) and page_goods_nums >= 60:

		break

		except Exception as e:

		print(f'{supply_name}商家，第{page_num}页面选择失败,或所有商品详情获取失败，错误信息:{e},现休息3秒后...重新操作！')

		time.sleep(3)

		for goods_info in goods_infos: # 选择商品

		goods_info = goods_info.text

		print(f'{supply_name}，第{page_num+1}页，第{goods_nums}个商品！')

		with open(r'C:\Users\25808\Desktop\python_work\数据\药师邦.csv', 'a+', encoding='utf-8-sig',newline='') as f:

		date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

		data = [supply_name, goods_info, date]

		goods_nums = goods_nums + 1

		csv.writer(f).writerow(data)

		else:

		if goods_nums >= int(html_goods_nums):

		print(f'{supply_name}，页面商品数{html_goods_nums}个，实际下载{goods_nums},全部下载完成！')

		with open(r'C:\Users\25808\Desktop\python_work\数据\sup_complete.txt', 'a') as f:

		f.write(f'{supply_name}，页面商品数{html_goods_nums}个，实际下载{goods_nums},全部下载完成！这是第{s+1}个商家！\r\n')

		else:

		print(f'{supply_name}，页面商品数{html_goods_nums}个，实际下载{goods_nums},少下载了{goods_nums-int(html_goods_nums)}个！')

		with open(r'C:\Users\25808\Desktop\python_work\数据\sup_complete.txt', 'a') as f:

		f.write(f'{supply_name}，页面商品数{html_goods_nums}个，实际下载{goods_nums},少下载了{goods_nums-int(html_goods_nums)}个！这是第{s+1}个商家！\r\n')

		vars = ['goods_info', 'goods_index', 'goods_infos', 'supply_name', 'goods_nums']

		for x in [k for k, v in globals().items() if k in vars]:

		globals().pop(x)



	def asyn_sup(self,cookies):

		self.executor.submit(self.main, driver=self.driver1, cookies=cookies)

		self.executor.submit(self.main, driver=self.driver2, cookies=cookies)

		self.executor.submit(self.main, driver=self.driver3, cookies=cookies)

		self.executor.submit(self.main, driver=self.driver4, cookies=cookies)



	def run(self):

		self.get_target_page()

		cookies = self.driver.get_cookies()

		self.driver.close()

		self.asyn_sup(cookies)





if __name__ == '__main__':

	run = Yaosb()

	run.run()