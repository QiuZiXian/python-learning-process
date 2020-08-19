# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# # __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# # @time          :2020/7/5  14:49
# # @abstract    :
#
#
#  # %matplotlib inline
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import emcee
# x,y, yerr = np.loadtxt("./ch1.txt", unpack = True)
# print(x)
# plt.errorbar(x,y,yerr, fmt="o")
# def f(x, A, t1,t2,ts):
#     if (x>ts).any():
#         c = np.exp(2*(t1/t2)^(1/2))
#         a = A*np.exp(2*(t1/t2)**(1/2))
#         b = np.exp((-t1/(x-ts))-((x-ts)/t2))
#         return a*b
#     else:
#         return -np.inf
#
# #
# # def test1():
# #
# #     if x > 1:
# #         print(1)
# #
# # def test2():
# #     test1()
# #
# # test2()
# # print(x> 1)
# # print((x > 1).any())
# # model y = ax + b
# a, b = 0, 0
# theta = (a,b)
# def lnlike(theta, x, y, yerr):
#     # log(likelihood)
#     # likelihood = exp(-chi^2/2)
#     # log(likelihood) = -chi^2/2
#     A,t1,t2,ts = theta
#     chi2 = np.sum((y - f(x, A,t1,t2,ts))**2/yerr**2)
#     # print "chi2:", chi2
#     return -0.5*chi2
#
# ndim, nwalkers = 4, 100
#
#
# A_init = 100
# t1_init = 30
# t2_init = 20
# ts_init = 50
# theta_init = np.array([A_init,t1_init,t2_init,ts_init])
#
#
# pos = [theta_init + 5e-1*np.random.randn(ndim) for i in range(nwalkers)]
#
# sampler = emcee.EnsembleSampler(nwalkers, ndim, lnlike, args=(x, y, yerr))
# sampler.run_mcmc(pos, 100)

import numpy as np
import sympy

tmp = np.linspace(0, 1, 21)
print(type(tmp))
print(tmp)

print(sympy.S.Reals)
I = sympy.Interval(0,sympy.oo)
print(I)

print("abc".split())
for i in "abd":
	print(i)


import os
print(os.getcwd())



import random
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
c_1 = np.random.multivariate_normal([0,0], np.diag([1,1]), 50)
c_2 = np.random.multivariate_normal([2,2], np.diag([1,1]), 50)

label = np.asarray([0]*len(c_1) + [1]*len(c_2))
lda_data = np.row_stack([c_1, c_2])
shuffle_index = np.arange(len(lda_data))
random.shuffle(shuffle_index)
lda_data = lda_data[shuffle_index]
label = label[shuffle_index]
lda = LinearDiscriminantAnalysis()
result = lda.fit(lda_data, label)