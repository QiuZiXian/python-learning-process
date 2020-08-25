# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/19  20:38
# @abstract    :

from tkinter import *

amount = 10000


# ..............Dashboard.............................
def Dashboard():
	# .........Debit.....................
	def Debit():

		def Submit():
			global amount

			if (int(e.get()) < amount):
				amount = amount - int(e.get())
				print(amount)
				Dashboard()
				DQuit()
				DeQuit()

			else:
				amount = amount
				print('enter correct values')
				Dashboard()
				DeQuit()

		def DeQuit():
			root.destroy()

		root = Toplevel()
		l = Label(root, text='Amount').grid(row=0)
		e = Entry(root)
		e.grid(row=0, column=1)
		b1 = Button(root, text='Submit', command=Submit).grid(row=1)
		b2 = Button(root, text='Quit', command=DeQuit).grid(row=1, column=1)

	# .................Credit...........................
	def Credit():

		def Submit():
			global amount
			amount = amount + int(e.get())
			print(amount)
			Dashboard()
			DQuit()
			DQuit()

		def CrQuit():
			root.destroy()

		root = Toplevel()
		l = Label(root, text='Amount').grid(row=0)
		e = Entry(root)
		e.grid(row=0, column=1)
		b1 = Button(root, text='Submit', command=Submit).grid(row=1)
		b2 = Button(root, text='Quit', command=CrQuit).grid(row=1, column=1)

	def DQuit():
		root.destroy()

	root = Toplevel()
	l = Label(root, text='Balance').grid(row=0)
	l = Label(root, text=amount).grid(row=0, column=1)
	b1 = Button(root, text='Debit', command=Debit).grid(row=1)
	b2 = Button(root, text='Credit', command=Credit).grid(row=1, column=1)
	b3 = Button(root, text='Quit', command=DQuit).grid(row=2, column=0)


# ..............Verification..........................
def Submit():
	if (e1.get() == 'anish' and e2.get() == '1234'):
		Dashboard()
	else:
		print('enter correct info')


# .......Destroying the main login window..............
def MQuit():
	root.destroy()


root = Tk()

l = Label(root, text='Username:').grid(row=0)
l = Label(root, text='Password:').grid(row=1)

e1 = Entry()
e1.grid(row=0, column=1)
e2 = Entry()
e2.grid(row=1, column=1)

b1 = Button(root, text='Submit', command=Submit).grid(row=2)
b2 = Button(root, text='Quit', command=MQuit).grid(row=2, column=1)

root.mainloop()