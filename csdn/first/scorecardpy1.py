# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:03:21 2020

@author: 87875
"""

# Traditional Credit Scoring Using Logistic Regression
import scorecardpy as sc
import matplotlib.pyplot as plt

# data prepare ------
# load germancredit data
dat = sc.germancredit()

# filter variable via missing rate, iv, identical value rate
dt_s = sc.var_filter(dat, y="creditability")

# breaking dt into train and test
train, test = sc.split_df(dt_s, 'creditability').values()

# woe binning ------
bins = sc.woebin(dt_s, y="creditability")
print(type(bins))
for k,v in bins.items():
	print(k)

print(bins["purpose"])
print(bins["purpose"].columns)
print(type(bins["purpose"]))
# sc.woebin_plot(bins["purpose"])
# plt.show()


# =============================================================================
# print("qq: 1467288927")
# =============================================================================
