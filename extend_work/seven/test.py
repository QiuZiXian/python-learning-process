# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/9  16:17
# @abstract    :

aero = {}
for i in range(1,3):
    aero['预警指挥机'+str(i)] = ['A','B','D','E']
aero['电子战机'] = ['C','E']
for i in range(1,3):
    aero['歼击机'+str(i)] = ['A','B','E']
print(aero)

sarr = [{}]
for n,a in aero.items():
    tarr = [];
    for b in sarr:
        for c in a:
            s = b.copy()
            s[n] = c
            tarr.append(s);
    sarr = tarr;
for d in sarr:
    print(d)