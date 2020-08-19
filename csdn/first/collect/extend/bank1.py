# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/18  23:04
# @abstract    :

import random

class Account():
	'''
	简单的用户atm操作模拟-单文件
	扩展方向：1、数据、验证、操作分开
		2、函数私有，只开放主函数
		3、数据接入本地或数据库
		4、接入gui
		5、打包成exe
	'''

	def __init__(self):
		self.id = 0  # 用户id
		self.usersAccount = {i: 100 for i in range(10)} # 简单的用户账号数据记录, 数据存储单独拉一个类
		self.choice = 0  # 主菜单选项初始化参数
		self.isStop = False # 控制该用户是否继续操作，即用户进入后一直keep alive

	def initUser(self, id):
		# 由于只用了一个文件，需要每个用户进入都要对其初始化
		self.isStop = False
		self.id = id

	def initView(self): # 初始化界面

		print("===============================")
		print("===========主菜单==============")
		print("=========1：查询余额===========")
		print("=========2：取款===============")
		print("=========3： 存款==============")
		print("=========4： 退出==============")
		self.choice = input("请输入你的选项：")

	def selectAcout(self):
		print("您的余额为：",self.usersAccount[self.id])

	def deposit(self):
		print("正在存钱。。。")
		money = random.sample([100, 200, 1000, 100000, 500], 1)[0]  # 这里用随机模拟存钱
		self.usersAccount[self.id] = self.usersAccount[self.id] + money
		print("您存入了", money, "元，此时：")
		self.selectAcout()

	def withdrawal(self,money):
		print("正在取钱。。。")
		self.usersAccount[self.id] = self.usersAccount[self.id] - money
		print("您取出了", money, "元，此时：")
		self.selectAcout()

	def stop(self):
		self.isStop = True

	def verify(self): # 可扩展，并且单独放置在功能模块
		'''
		键盘外接收值是否 异常值判断
		:return:
		'''
		self.choice = int(self.choice)
		pass
	def poor(self, money): # 取钱前要 先验证账号是否有足够余额
		if self.usersAccount[self.id] - money >= 0:
			return self.usersAccount[self.id] - money
		else:
			return False

	def choose(self): # 可优化if语句
		if self.choice == 4:
			self.stop()
		elif self.choice == 1:
			self.selectAcout()
		elif self.choice == 3:
			self.deposit()
		elif self.choice == 2:
			money = random.sample([100, 200, 1000, 100000, 500], 1)[0]  # 这里用随机模拟存钱
			if self.poor(money):
				self.withdrawal(money)
			else:
				print("您想取", money, "元，但是：")
				print("您穷的叮当响啊！！！")

	def main(self):
		self.initView()
		self.verify()
		self.choose()


if __name__ == '__main__':
	demo = Account()
	while True:
		id = int(input("请输入用户id："))
		demo.initUser(id)  # 这个也可以放在demo.main()里面，但理论上要保证其只初始化一次
		while True:
			if demo.isStop:
				break
			demo.main()
