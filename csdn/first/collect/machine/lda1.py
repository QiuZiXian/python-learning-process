# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/17  20:36
# @abstract    :

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

result.coef_