# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/9  12:07
# @abstract    :


task_1 = ['A', 'B', 'D', 'E']
task_2 = [ 'C', 'E']
task_3 = ['A', 'B',  'E']
for i in range(2):
	for t1 in task_1:


		pass





# for t in permutations(task_1, 2):
# 	print(t)
#
# for t in permutations(task_2, 1):
# 	print(t)

# for t in permutations(list(range(10))):
# 	print(t)

# p1 = [[]] *4*4
#
# for p in range(2):
# 	for i in range(4):
# 		p.append([i])
#
# print(p)
# p2 = []
# # for i in range(2):
# # 	for item in p:
# # 		p2.append(item.append(i))
# # print(p2)
# from copy import deepcopy
#
# p2 = [p, deepcopy(p)]
# for i in range(2):
# 	for item in p2[i]:
# 		item.append(i)
#
# print(p2)
#
#
# p3 = [[]]*10
# for a in range(10):
# 	for i in range(3):
# 		p3[a].append(i)
# print(p3)

# for i in range(4):
# 	for j in range(4):
# 		print(i, j)


from itertools import product

for t1 in product('ABDE', repeat=2):#
	print(t1)

# 三种情况 分三步 取
# for t1 in product('ABDE', repeat=2):#
#    for t2 in 'CE':
#       for t3 in product('ABE', repeat=10):
#          # 汇总三步取 的结果
#          opt = list(t1)
#          opt.append(t2)
#          opt.extend(list(t3))
#          print(opt)



